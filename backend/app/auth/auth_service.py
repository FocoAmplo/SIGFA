import secrets
from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException, Request, status
from sqlalchemy.orm import Session

from ..auth.jwt_handler import create_access_token
from ..auth.password import verify_password
from ..models.login_audit import LoginAudit
from ..models.refresh_token import RefreshToken
from ..models.user import User


class AuthService:
    REFRESH_TOKEN_EXPIRE_DAYS = 14
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    def authenticate_user(
        self,
        db: Session,
        email: str,
        senha: str,
        request: Request,
    ) -> dict:
        user = db.query(User).filter(User.email == email).first()
        audit_reason = None

        if user is None:
            audit_reason = "Usuário não encontrado"
            self._create_login_audit(db, None, email, False, audit_reason, request)
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

        if not user.active:
            audit_reason = "Usuário inativo"
            self._create_login_audit(db, user.id, email, False, audit_reason, request)
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário inativo")

        if not verify_password(senha, user.password_hash):
            audit_reason = "Senha inválida"
            self._create_login_audit(db, user.id, email, False, audit_reason, request)
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

        access_token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
                "name": user.name,
                "company_id": user.company_id,
            }
        )
        refresh_token = self._create_refresh_token(db, user, request)
        user.last_login = datetime.utcnow()
        db.add(user)
        db.commit()

        self._create_login_audit(db, user.id, email, True, None, request)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token.token,
            "token_type": "bearer",
            "expires_at": datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES),
        }

    def refresh_access_token(self, db: Session, refresh_token_value: str, request: Request) -> dict:
        token_record = db.query(RefreshToken).filter(RefreshToken.token == refresh_token_value).first()
        if token_record is None or token_record.revoked:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token inválido")

        if token_record.expires_at < datetime.utcnow():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token expirado")

        user = token_record.user
        if user is None or not user.active:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário inválido")

        token_record.revoked = True
        db.add(token_record)
        db.commit()

        new_refresh_token = self._create_refresh_token(db, user, request)
        access_token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
                "name": user.name,
                "company_id": user.company_id,
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_at": datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES),
        }

    def logout_user(self, db: Session, refresh_token_value: str) -> None:
        token_record = db.query(RefreshToken).filter(RefreshToken.token == refresh_token_value).first()
        if token_record is None or token_record.revoked:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Refresh token não encontrado")

        token_record.revoked = True
        db.add(token_record)
        db.commit()

    def _create_refresh_token(self, db: Session, user: User, request: Request) -> RefreshToken:
        token_value = secrets.token_urlsafe(32)
        expires_at = datetime.utcnow() + timedelta(days=self.REFRESH_TOKEN_EXPIRE_DAYS)
        refresh_token = RefreshToken(
            token=token_value,
            user_id=user.id,
            expires_at=expires_at,
        )
        db.add(refresh_token)
        db.commit()
        db.refresh(refresh_token)
        return refresh_token

    def _create_login_audit(
        self,
        db: Session,
        user_id: Optional[int],
        email: str,
        success: bool,
        reason: Optional[str],
        request: Request,
    ) -> None:
        audit = LoginAudit(
            user_id=user_id,
            email=email,
            success=success,
            reason=reason,
            ip_address=request.client.host if request.client else None,
            user_agent=request.headers.get("User-Agent", ""),
        )
        db.add(audit)
        db.commit()
