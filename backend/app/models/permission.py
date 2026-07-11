from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class Permission(Base):

    __tablename__ = "permissions"
    __table_args__ = {"schema": "security"}

    id = Column(Integer, primary_key=True, index=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()")
    )

    code = Column(String(80), unique=True)

    name = Column(String(150))

    description = Column(String)

    module = Column(String(100))

    active = Column(Boolean, default=True)

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP")
    )