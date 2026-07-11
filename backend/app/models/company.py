from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class Company(Base):

    __tablename__ = "company"
    __table_args__ = {"schema": "sigfa"}

    id = Column(Integer, primary_key=True, index=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
        nullable=False,
    )

    corporate_name = Column(String(250), nullable=False)

    trade_name = Column(String(200))

    cnpj = Column(String(18))

    state_registration = Column(String(30))

    municipal_registration = Column(String(30))

    segment = Column(String(120))

    employees = Column(Integer, default=0)

    city = Column(String(120))

    state = Column(String(2))

    country = Column(String(80), default="Brasil")

    phone = Column(String(30))

    email = Column(String(200))

    website = Column(String(200))

    active = Column(Boolean, default=True)

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

    users = relationship(
        "User",
        back_populates="company",
        cascade="all, delete-orphan",
    )

    diagnosis = relationship(
        "Diagnosis",
        back_populates="company",
        cascade="all, delete-orphan",
    )

    notifications = relationship(
        "Notification",
        back_populates="company",
        cascade="all, delete-orphan",
    )