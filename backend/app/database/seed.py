from datetime import datetime

from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import text
from sqlalchemy.orm import Session

from .config import engine
from .session import SessionLocal
from ..auth.password import hash_password
from ..models.base import Base
from ..models.company import Company
from ..models.permission import Permission
from ..models.profile import Profile
from ..models.user import User
from ..models.omc import OMC
from ..models.concept import Concept
from ..models.method import Method
from ..models.tool import Tool
from ..models.kpi import KPI
from ..models.question import Question
from ..models.evidence import Evidence
from ..models.risk import Risk
from ..models.recommendation import Recommendation
from ..models.relationship import Relationship
from ..models.diagnosis import Diagnosis
from ..models.answer import Answer
from ..models.score import Score
from ..models.action_plan import ActionPlan
from ..models.attachment import Attachment
from ..models.history import History
from ..models.ai_recommendation import AIRecommendation
from ..models.dashboard import Dashboard
from ..models.card import Card
from ..models.chart import Chart
from ..models.filter import Filter

ADMIN_EMAIL = "admin@sigfa.com.br"
ADMIN_PASSWORD = "Admin123!"
COMPANY_NAME = "SIGFA Corporativo"
ADMIN_PROFILE = "Administrador"

POSTGRES_SCHEMAS = [
    "sigfa",
    "security",
    "knowledge",
    "diagnosis",
    "dashboard",
    "logs",
]

CORE_TABLES = [
    Company.__table__,
    Profile.__table__,
    Permission.__table__,
    User.__table__,
    OMC.__table__,
    Concept.__table__,
    Method.__table__,
    Tool.__table__,
    KPI.__table__,
    Question.__table__,
    Evidence.__table__,
    Risk.__table__,
    Recommendation.__table__,
    Relationship.__table__,
    Diagnosis.__table__,
    Answer.__table__,
    Score.__table__,
    ActionPlan.__table__,
    Attachment.__table__,
    History.__table__,
    AIRecommendation.__table__,
    Dashboard.__table__,
    Card.__table__,
    Chart.__table__,
    Filter.__table__,
]


def create_database() -> None:
    with engine.begin() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS pgcrypto"))

        for schema in POSTGRES_SCHEMAS:
            connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema}"))

    Base.metadata.create_all(bind=engine, tables=CORE_TABLES)


def seed_initial_data() -> None:
    db: Session = SessionLocal()
    try:
        connection = db.connection()

        company = connection.execute(
            select(Company.__table__.c.id).where(
                Company.__table__.c.corporate_name == COMPANY_NAME
            )
        ).first()
        if not company:
            result = connection.execute(
                insert(Company.__table__)
                .values(
                    corporate_name=COMPANY_NAME,
                    trade_name="SIGFA",
                    cnpj="00.000.000/0001-00",
                    city="Sede SIGFA",
                    country="Brasil",
                    active=True,
                )
                .returning(Company.__table__.c.id)
            )
            company_id = result.scalar_one()
        else:
            company_id = company.id

        admin_profile = connection.execute(
            select(Profile.__table__.c.id).where(
                Profile.__table__.c.name == ADMIN_PROFILE
            )
        ).first()
        if not admin_profile:
            result = connection.execute(
                insert(Profile.__table__)
                .values(
                    name=ADMIN_PROFILE,
                    description="Administrador do sistema",
                    active=True,
                )
                .returning(Profile.__table__.c.id)
            )
            profile_id = result.scalar_one()
        else:
            profile_id = admin_profile.id

        permissions = [
            ("auth:login", "Login", "Login e emissão de token", "auth"),
            ("auth:refresh", "Refresh", "Refresh de token", "auth"),
            ("auth:logout", "Logout", "Logout e invalidação de refresh token", "auth"),
            ("user:read", "Leitura de usuário", "Leitura de dados do usuário", "user"),
        ]

        for code, name, description, module in permissions:
            permission = connection.execute(
                select(Permission.__table__.c.id).where(
                    Permission.__table__.c.code == code
                )
            ).first()
            if not permission:
                connection.execute(
                    insert(Permission.__table__).values(
                        code=code,
                        name=name,
                        description=description,
                        module=module,
                        active=True,
                    )
                )

        admin_user = connection.execute(
            select(User.__table__.c.id).where(
                User.__table__.c.email == ADMIN_EMAIL
            )
        ).first()
        if not admin_user:
            connection.execute(
                insert(User.__table__).values(
                    name="Administrador SIGFA",
                    email=ADMIN_EMAIL,
                    password_hash=hash_password(ADMIN_PASSWORD),
                    company_id=company_id,
                    profile_id=profile_id,
                    active=True,
                    last_login=datetime.utcnow(),
                )
            )

        db.commit()
    finally:
        db.close()
