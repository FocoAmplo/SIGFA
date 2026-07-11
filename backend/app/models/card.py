from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class Card(Base):

    __tablename__ = "cards"
    __table_args__ = {"schema": "dashboard"}

    id = Column(Integer, primary_key=True)

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
        nullable=False,
    )

    dashboard_id = Column(
        Integer,
        ForeignKey("dashboard.dashboards.id"),
        nullable=False,
    )

    code = Column(String(30))

    title = Column(String(200))

    metric_code = Column(String(30))

    icon = Column(String(100))

    color = Column(String(50))

    position = Column(Integer)

    active = Column(
        Boolean,
        default=True,
    )

    dashboard = relationship(
        "Dashboard",
        back_populates="cards",
    )