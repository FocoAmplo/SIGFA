from fastapi import HTTPException, Request, status
from sqlalchemy.orm import Session

from ..models.company import Company
from ..models.role import RoleType
from ..models.user import User
from ..auth.password import hash_password
from .jwt_handler import create_access_token


class ExternalAuthService:
    def authenticate(self, db: Session, email: str, name: str | None, provider: str, request: Request) -> dict:
        user = db.query(User).filter(User.email == email).first()

        if user is None:
            company = db.query(Company).first()
            if company is None:
                company = Company(nome="SIGFA Corporativo", cnpj="00.000.000/0001-00", endereco="Sede SIGFA")
                db.add(company)
                db.commit()
                db.refresh(company)

            role = db.query(User.role.property.mapper.class_).first() if False else None
            if role is None:
                from ..models.role import Role
                role = db.query(Role).filter(Role.nome == RoleType.Administrador.value).first()
            if role is None:
                role = Role(nome=RoleType.Administrador.value, descricao="Administrador do sistema")
                db.add(role)
                db.commit()
                db.refresh(role)

            user = User(
                nome=name or email.split('@')[0],
                email=email,
                senha_hash=hash_password('ExternalAuth123!'),
                empresa_id=company.id,
                role_id=role.id,
                ativo=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        permissions = []
        if user.role and user.role.permissions:
            permissions = [permission.chave for permission in user.role.permissions]

        access_token = create_access_token({
            "sub": str(user.id),
            "email": user.email,
            "nome": user.nome,
            "role": user.role.nome if user.role else "",
            "empresa_id": user.empresa_id,
            "permissions": permissions,
        })

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "provider": provider,
        }
