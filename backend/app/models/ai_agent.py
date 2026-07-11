from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class AIAgent(Base):

    __tablename__ = "ai_agents"
    __table_args__ = {"schema": "knowledge"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
        nullable=False,
    )

    code = Column(
        String(30),
        unique=True,
        nullable=False,
    )

    name = Column(
        String(200),
        nullable=False,
    )

    specialty = Column(String(150))

    description = Column(Text)

    model_name = Column(String(100))

    version = Column(
        String(20),
        default="1.0",
    )

    active = Column(
        Boolean,
        default=True,
    )

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    updated_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    memories = relationship(
        "AIMemory",
        back_populates="agent",
        cascade="all, delete-orphan",
    )

    prompts = relationship(
        "AIPrompt",
        back_populates="agent",
        cascade="all, delete-orphan",
    )