import secrets
from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException, Request, status
from sqlalchemy.orm import Session

from ..auth.jwt_handler import create_access_token
from ..auth.password import hash_password, verify_password
from ..models.company import Company
from ..models.login_audit import LoginAudit
from ..models.permission import Permission
from ..models.refresh_token import RefreshToken
from ..models.role import Role, RoleType
from ..models.session import UserSession
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

        if not user.ativo:
            audit_reason = "Usuário inativo"
            self._create_login_audit(db, user.id, email, False, audit_reason, request)
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário inativo")

        if not verify_password(senha, user.senha_hash):
            audit_reason = "Senha inválida"
            self._create_login_audit(db, user.id, email, False, audit_reason, request)
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

        permissions = self._build_permissions(user)
        access_token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
                "nome": user.nome,
                "role": user.role.nome if user.role else "",
                "empresa_id": user.empresa_id,
                "permissions": permissions,
            }
        )
        refresh_token = self._create_refresh_token(db, user, request)
        user.ultimo_login = datetime.utcnow()
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
        session = db.query(RefreshToken).filter(RefreshToken.token == refresh_token_value).first()
        if session is None or session.revoked:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token inválido")

        if session.expires_at < datetime.utcnow():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token expirado")

        user = session.user
        if user is None or not user.ativo:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário inválido")

        session.revoked = True
        if session.user_session is not None:
            session.user_session.revoked = True
            session.user_session.last_active = datetime.utcnow()
            db.add(session.user_session)

        db.add(session)
        db.commit()

        new_refresh_token = self._create_refresh_token(db, user, request)
        permissions = self._build_permissions(user)
        access_token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
                "nome": user.nome,
                "role": user.role.nome if user.role else "",
                "empresa_id": user.empresa_id,
                "permissions": permissions,
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_at": datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES),
        }

    def logout_user(self, db: Session, refresh_token_value: str) -> None:
        session = db.query(RefreshToken).filter(RefreshToken.token == refresh_token_value).first()
        if session is None or session.revoked:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Refresh token não encontrado")

        session.revoked = True
        if session.user_session is not None:
            session.user_session.revoked = True
            db.add(session.user_session)

        db.add(session)
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

        user_session = UserSession(
            user_id=user.id,
            refresh_token_id=refresh_token.id,
            ip_address=request.client.host if request.client else None,
            user_agent=request.headers.get("User-Agent", ""),
        )
        db.add(user_session)
        db.commit()
        db.refresh(user_session)

        refresh_token.user_session = user_session
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

    def _build_permissions(self, user: User) -> list[str]:
        if user.role and user.role.permissions:
            return [permission.chave for permission in user.role.permissions]
        return []
