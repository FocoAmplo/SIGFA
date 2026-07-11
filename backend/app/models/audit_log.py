from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import text

from .base import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"
    __table_args__ = {"schema": "logs"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
    )

    user_id = Column(Integer)

    module = Column(String(100))

    action = Column(String(100))

    table_name = Column(String(100))

    record_id = Column(Integer)

    old_data = Column(JSONB)

    new_data = Column(JSONB)

    ip_address = Column(String(50))

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )