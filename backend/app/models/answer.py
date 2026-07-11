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


class Answer(Base):

    __tablename__ = "answers"
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

    question_code = Column(String(30))

    answer = Column(Text)

    score = Column(Numeric(6, 2))

    observation = Column(Text)

    evidence_file = Column(Text)

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    diagnosis = relationship(
        "Diagnosis",
        back_populates="answers",
    )