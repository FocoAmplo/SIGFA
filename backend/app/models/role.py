from enum import Enum

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class RoleType(str, Enum):
    Administrador = "Administrador"
    Consultor = "Consultor"
    Gestor = "Gestor"
    Colaborador = "Colaborador"


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), unique=True, nullable=False)
    descricao = Column(String(255), nullable=True)

    users = relationship("User", back_populates="role")
    permissions = relationship("Permission", secondary="role_permissions", back_populates="roles")
