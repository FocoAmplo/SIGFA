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


class Concept(Base):

    __tablename__ = "concepts"
    __table_args__ = {"schema": "knowledge"}

    id = Column(Integer, primary_key=True, index=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
        nullable=False,
    )

    omc_id = Column(
        Integer,
        ForeignKey("knowledge.omc.id"),
        nullable=False,
    )

    code = Column(
        String(30),
        unique=True,
        nullable=False,
    )

    name = Column(
        String(250),
        nullable=False,
    )

    definition = Column(Text)

    objective = Column(Text)

    process = Column(String(150))

    area = Column(String(150))

    domain = Column(String(150))

    keywords = Column(Text)

    embedding = Column(Text)

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

    omc = relationship(
        "OMC",
        back_populates="concepts",
    )