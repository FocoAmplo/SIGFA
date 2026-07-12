from fastapi import HTTPException, Request, status
from sqlalchemy.orm import Session
from ..models.company import Company
from ..models.user import User
from ..auth.password import hash_password
from .jwt_handler import create_access_token
class ExternalAuthService:
    def authenticate(self, db: Session, email: str, name: str | None, provider: str, request: Request) -> dict:
        user = db.query(User).filter(User.email == email).first()

        if user is None:
            company = db.query(Company).first()
            if company is None:
                company = Company(corporate_name="SIGFA Corporativo", cnpj="00.000.000/0001-00")
                db.add(company)
                db.commit()
                db.refresh(company)

            user = User(
                name=name or email.split('@')[0],
                email=email,
                password_hash=hash_password('ExternalAuth123!'),
                company_id=company.id,
                active=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        access_token = create_access_token({
            "sub": str(user.id),
            "email": user.email,
            "name": user.name,
            "company_id": user.company_id,
        })

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "provider": provider,
        }
