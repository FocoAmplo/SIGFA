from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class Dashboard(Base):

    __tablename__ = "dashboards"
    __table_args__ = {"schema": "dashboard"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
        nullable=False,
    )

    code = Column(
        String(30),
        unique=True,
    )

    name = Column(
        String(200),
    )

    description = Column(Text)

    active = Column(
        Boolean,
        default=True,
    )

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    cards = relationship(
        "Card",
        back_populates="dashboard",
        cascade="all, delete-orphan",
    )

    charts = relationship(
        "Chart",
        back_populates="dashboard",
        cascade="all, delete-orphan",
    )

    filters = relationship(
        "Filter",
        back_populates="dashboard",
        cascade="all, delete-orphan",
    )