from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class KPI(Base):

    __tablename__ = "kpis"
    __table_args__ = {"schema": "knowledge"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
    )

    omc_id = Column(
        Integer,
        ForeignKey("knowledge.omc.id"),
        nullable=False,
    )

    code = Column(String(30), unique=True, nullable=False)

    name = Column(String(250), nullable=False)

    description = Column(Text)

    formula = Column(Text)

    unit = Column(String(50))

    target_value = Column(Numeric(12,2))

    warning_value = Column(Numeric(12,2))

    critical_value = Column(Numeric(12,2))

    frequency = Column(String(50))

    keywords = Column(Text)

    embedding = Column(Text)

    version = Column(String(20), default="1.0")

    active = Column(Boolean, default=True)

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    updated_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    omc = relationship(
        "OMC",
        back_populates="kpis",
    )