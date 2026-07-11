from sqlalchemy import Boolean
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


class AIPrompt(Base):

    __tablename__ = "ai_prompts"
    __table_args__ = {"schema": "knowledge"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
    )

    agent_id = Column(
        Integer,
        ForeignKey("knowledge.ai_agents.id"),
    )

    title = Column(String(250))

    prompt = Column(Text)

    version = Column(String(20))

    active = Column(Boolean, default=True)

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    agent = relationship(
        "AIAgent",
        back_populates="prompts",
    )