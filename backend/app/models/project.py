from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    empresa_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False,
    )

    codigo = Column(String(30), unique=True, nullable=False, index=True)

    nome = Column(String(180), nullable=False)

    descricao = Column(Text)

    status = Column(
        String(50),
        default="Planejamento",
        nullable=False,
    )

    responsavel = Column(String(180))

    data_inicio = Column(DateTime)

    data_fim = Column(DateTime)

    ativo = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    empresa = relationship("Company", back_populates="projects")