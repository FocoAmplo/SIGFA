from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class Diagnosis(Base):

    __tablename__ = "diagnoses"
    __table_args__ = {"schema": "diagnosis"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
    )

    company_id = Column(
        Integer,
        ForeignKey("sigfa.company.id"),
        nullable=False,
    )

    title = Column(String(250))

    omc_code = Column(String(30))

    status = Column(
        String(30),
        default="OPEN",
    )

    score = Column(Numeric(6, 2))

    maturity_level = Column(Numeric(6, 2))

    risk_level = Column(String(30))

    started_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    finished_at = Column(DateTime)

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    updated_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    company = relationship("Company")

    answers = relationship(
        "Answer",
        back_populates="diagnosis",
        cascade="all, delete-orphan",
    )

    scores = relationship(
        "Score",
        back_populates="diagnosis",
        cascade="all, delete-orphan",
    )

    action_plans = relationship(
        "ActionPlan",
        back_populates="diagnosis",
        cascade="all, delete-orphan",
    )

    attachments = relationship(
        "Attachment",
        back_populates="diagnosis",
        cascade="all, delete-orphan",
    )

    history = relationship(
        "History",
        back_populates="diagnosis",
        cascade="all, delete-orphan",
    )