from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from .session import SessionLocal
from ..auth.password import hash_password
from ..models.base import Base
from ..models.company import Company
from ..models.document import Document
from ..models.permission import Permission
from ..models.role import Role, RoleType
from ..models.user import User
from ..models.project import Project

ADMIN_EMAIL = "admin@sigfa.com.br"
ADMIN_PASSWORD = "Admin123!"
COMPANY_NAME = "SIGFA Corporativo"


def create_database() -> None:
    Base.metadata.create_all(bind=engine)


def seed_initial_data() -> None:
    db: Session = SessionLocal()
    try:
        company = db.query(Company).filter_by(nome=COMPANY_NAME).first()
        if not company:
            company = Company(nome=COMPANY_NAME, cnpj="00.000.000/0001-00", endereco="Sede SIGFA")
            db.add(company)
            db.commit()
            db.refresh(company)

        admin_role = db.query(Role).filter_by(nome=RoleType.Administrador.value).first()
        if not admin_role:
            admin_role = Role(nome=RoleType.Administrador.value, descricao="Administrador do sistema")
            manager_role = Role(nome=RoleType.Gestor.value, descricao="Gestor de operações")
            consultant_role = Role(nome=RoleType.Consultor.value, descricao="Consultor corporativo")
            collaborator_role = Role(nome=RoleType.Colaborador.value, descricao="Colaborador interno")
            db.add_all([admin_role, manager_role, consultant_role, collaborator_role])
            db.commit()
            db.refresh(admin_role)

        permissions = [
            ("auth:login", "Login e emissão de token"),
            ("auth:refresh", "Refresh de token"),
            ("auth:logout", "Logout e invalidação de refresh token"),
            ("user:read", "Leitura de dados do usuário"),
        ]

        for chave, descricao in permissions:
            if not db.query(Permission).filter_by(chave=chave).first():
                db.add(Permission(chave=chave, descricao=descricao))
        db.commit()

        admin_user = db.query(User).filter_by(email=ADMIN_EMAIL).first()
        if not admin_user:
            admin_user = User(
                nome="Administrador SIGFA",
                email=ADMIN_EMAIL,
                senha_hash=hash_password(ADMIN_PASSWORD),
                empresa_id=company.id,
                role_id=admin_role.id,
                ativo=True,
                ultimo_login=datetime.utcnow(),
            )
            db.add(admin_user)
            db.commit()
    finally:
        db.close()
