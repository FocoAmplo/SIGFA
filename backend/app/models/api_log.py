from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text

from .base import Base


class APILog(Base):

    __tablename__ = "api_logs"
    __table_args__ = {"schema": "logs"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
    )

    endpoint = Column(String(255))

    method = Column(String(20))

    status_code = Column(Integer)

    execution_time_ms = Column(Numeric(10,2))

    user_id = Column(Integer)

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )