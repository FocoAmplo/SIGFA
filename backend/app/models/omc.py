from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class OMC(Base):

    __tablename__ = "omc"
    __table_args__ = {"schema": "knowledge"}

    id = Column(Integer, primary_key=True, index=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
        nullable=False,
    )

    code = Column(
        String(30),
        unique=True,
        nullable=False,
    )

    title = Column(
        String(250),
        nullable=False,
    )

    category = Column(String(150))

    subcategory = Column(String(150))

    objective = Column(Text)

    version = Column(
        String(20),
        default="1.0",
    )

    maturity_level = Column(
        Numeric(5, 2),
        default=0,
    )

    active = Column(
        Boolean,
        default=True,
    )

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    updated_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    concepts = relationship(
        "Concept",
        back_populates="omc",
        cascade="all, delete-orphan",
    )

    methods = relationship(
        "Method",
        back_populates="omc",
        cascade="all, delete-orphan",
    )

    tools = relationship(
        "Tool",
        back_populates="omc",
        cascade="all, delete-orphan",
    )

    kpis = relationship(
        "KPI",
        back_populates="omc",
        cascade="all, delete-orphan",
    )

    questions = relationship(
        "Question",
        back_populates="omc",
        cascade="all, delete-orphan",
    )

    evidences = relationship(
        "Evidence",
        back_populates="omc",
        cascade="all, delete-orphan",
    )

    risks = relationship(
        "Risk",
        back_populates="omc",
        cascade="all, delete-orphan",
    )

    recommendations = relationship(
        "Recommendation",
        back_populates="omc",
        cascade="all, delete-orphan",
    )