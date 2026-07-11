from sqlalchemy import Column, DateTime, Integer, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text

from .base import Base


class AILog(Base):

    __tablename__ = "ai_logs"
    __table_args__ = {"schema": "logs"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
    )

    agent_code = Column(String(30))

    diagnosis_id = Column(Integer)

    prompt = Column(Text)

    response = Column(Text)

    tokens = Column(Integer)

    execution_time_ms = Column(Numeric(10,2))

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )