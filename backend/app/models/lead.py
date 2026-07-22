from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class Lead(Base):

    __tablename__ = "lead"
    __table_args__ = {"schema": "sigfa"}

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
        nullable=False,
        unique=True,
    )

    name = Column(
        String(180),
        nullable=False,
    )

    email = Column(
        String(200),
        nullable=False,
        index=True,
    )

    phone = Column(
        String(30),
    )

    company_name = Column(
        String(250),
    )

    segment = Column(
        String(150),
    )

    city = Column(
        String(120),
    )

    state = Column(
        String(2),
    )

    employees = Column(
        Integer,
        default=0,
    )

    monthly_revenue = Column(
        Numeric(15, 2),
        default=0,
    )

    main_problem = Column(
        Text,
    )

    urgency = Column(
        Integer,
        default=1,
    )

    investment_capacity = Column(
        Integer,
        default=1,
    )

    score = Column(
        Integer,
        default=0,
        nullable=False,
    )

    classification = Column(
        String(50),
        default="não qualificado",
        nullable=False,
    )

    status = Column(
        String(50),
        default="novo",
        nullable=False,
    )

    source = Column(
        String(80),
        default="gpt_publico",
        nullable=False,
    )

    notes = Column(
        Text,
    )

    qualified = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    updated_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )