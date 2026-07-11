from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class History(Base):

    __tablename__ = "history"
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

    event_type = Column(String(100))

    description = Column(Text)

    user_name = Column(String(200))

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    diagnosis = relationship(
        "Diagnosis",
        back_populates="history",
    )