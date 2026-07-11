from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class Relationship(Base):

    __tablename__ = "relationships"
    __table_args__ = {"schema": "knowledge"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
    )

    source_type = Column(String(50))

    source_code = Column(String(30))

    target_type = Column(String(50))

    target_code = Column(String(30))

    relationship_type = Column(String(80))

    strength = Column(Numeric(5, 2))

    description = Column(Text)

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
    )