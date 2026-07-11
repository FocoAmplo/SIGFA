from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AIAgentBase(BaseModel):

    code: str

    name: str

    specialty: Optional[str] = None

    description: Optional[str] = None

    model_name: Optional[str] = None

    version: str = "1.0"

    active: bool = True


class AIAgentCreate(AIAgentBase):
    pass


class AIAgentUpdate(BaseModel):

    code: Optional[str] = None

    name: Optional[str] = None

    specialty: Optional[str] = None

    description: Optional[str] = None

    model_name: Optional[str] = None

    version: Optional[str] = None

    active: Optional[bool] = None


class AIAgentResponse(AIAgentBase):

    id: int

    uuid: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)