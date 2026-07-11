from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class AIRule(Base):

    __tablename__ = "ai_rules"
    __table_args__ = {"schema": "knowledge"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
    )

    code = Column(String(30), unique=True)

    title = Column(String(250))

    condition = Column(Text)

    action = Column(Text)

    priority = Column(Integer)

    active = Column(Boolean, default=True)

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )