from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    titulo = Column(String(180), nullable=False)
    descricao = Column(String(500), nullable=True)

    filename = Column(String(255), nullable=False)
    filepath = Column(String(500), nullable=False)

    empresa_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False,
    )

    uploaded_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    empresa = relationship(
        "Company",
        back_populates="documents",
    )

    uploader = relationship(
        "User",
        back_populates="documents",
    )