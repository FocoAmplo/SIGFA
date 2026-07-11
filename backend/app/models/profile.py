from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class Profile(Base):

    __tablename__ = "profiles"
    __table_args__ = {"schema": "security"}

    id = Column(Integer, primary_key=True, index=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()")
    )

    name = Column(String(100), nullable=False)

    description = Column(String)

    active = Column(Boolean, default=True)

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP")
    )

    users = relationship(
        "User",
        back_populates="profile"
    )