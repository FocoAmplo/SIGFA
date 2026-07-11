from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import text

from .base import Base


class Notification(Base):

    __tablename__ = "notifications"
    __table_args__ = {"schema": "logs"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
    )

    company_id = Column(
        Integer,
        ForeignKey("sigfa.company.id"),
    )

    title = Column(String(250))

    message = Column(Text)

    notification_type = Column(String(50))

    readed = Column(Boolean, default=False)

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    company = relationship(
        "Company",
        back_populates="notifications",
    )