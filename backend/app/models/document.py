from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, text
from sqlalchemy.dialects.postgresql import JSONB, UUID

from .base import Base


class Document(Base):
    __tablename__ = "documents"
    __table_args__ = {"schema": "intelligence"}

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), server_default=text("gen_random_uuid()"))

    tenant_id = Column(String(120), nullable=False)
    company_id = Column(Integer, ForeignKey("sigfa.company.id"), nullable=False)
    uploaded_by = Column(Integer, ForeignKey("security.users.id"), nullable=False)
    title = Column(String(180), nullable=False)
    description = Column(String(500), nullable=True)

    filename = Column(String(255), nullable=False)
    content_type = Column(String(120))
    content_hash = Column(String(128), nullable=False)
    storage_bucket = Column(String(255), nullable=False)
    storage_path = Column(Text, nullable=False)
    status = Column(String(40), nullable=False, default="STORED")
    metadata_ = Column("metadata", JSONB, nullable=False, server_default=text("'{}'::jsonb"))

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

