from sqlalchemy import Column
from sqlalchemy import Date
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


class ActionPlan(Base):

    __tablename__ = "action_plans"
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

    recommendation_code = Column(String(30))

    action_description = Column(Text)

    responsible = Column(String(200))

    due_date = Column(Date)

    priority = Column(String(30))

    status = Column(String(30), default="PENDING")

    progress = Column(Numeric(5,2), default=0)

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    updated_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    diagnosis = relationship(
        "Diagnosis",
        back_populates="action_plans",
    )