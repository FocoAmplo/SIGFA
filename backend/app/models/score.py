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


class Score(Base):

    __tablename__ = "scores"
    __table_args__ = {"schema": "diagnosis"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
    )

    diagnosis_id = Column(
        Integer,
        ForeignKey("diagnosis.diagnoses.id"),
        nullable=False,
    )

    indicator_code = Column(String(30))

    value = Column(Numeric(12, 2))

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    diagnosis = relationship(
        "Diagnosis",
        back_populates="scores",
    )