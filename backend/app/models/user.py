from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):

    __tablename__ = "users"
    __table_args__ = {"schema": "security"}

    id = Column(Integer, primary_key=True, index=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
        nullable=False,
    )

    company_id = Column(
        Integer,
        ForeignKey("sigfa.company.id"),
        nullable=False,
    )

    profile_id = Column(
        Integer,
        ForeignKey("security.profiles.id"),
        nullable=True,
    )

    name = Column(
        String(200),
        nullable=False,
    )

    email = Column(
        String(200),
        unique=True,
        nullable=False,
    )

    password_hash = Column(
        String,
        nullable=False,
    )

    phone = Column(
        String(30)
    )

    avatar = Column(
        String
    )

    last_login = Column(
        DateTime
    )

    active = Column(
        Boolean,
        default=True,
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

    company = relationship(
        "Company",
        back_populates="users",
    )

    profile = relationship(
        "Profile",
        back_populates="users",
    )