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


class AIMemory(Base):

    __tablename__ = "ai_memories"
    __table_args__ = {"schema": "knowledge"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
    )

    agent_id = Column(
        Integer,
        ForeignKey("knowledge.ai_agents.id"),
        nullable=False,
    )

    context = Column(Text)

    source_type = Column(String(50))

    source_code = Column(String(30))

    confidence = Column(Numeric(5,2))

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    agent = relationship(
        "AIAgent",
        back_populates="memories",
    )