from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AILogBase(BaseModel):

    agent_code: Optional[str] = None

    diagnosis_id: Optional[int] = None

    prompt: Optional[str] = None

    response: Optional[str] = None

    tokens: Optional[int] = None

    execution_time_ms: Optional[Decimal] = None


class AILogCreate(AILogBase):
    pass


class AILogUpdate(BaseModel):

    agent_code: Optional[str] = None

    diagnosis_id: Optional[int] = None

    prompt: Optional[str] = None

    response: Optional[str] = None

    tokens: Optional[int] = None

    execution_time_ms: Optional[Decimal] = None


class AILogResponse(AILogBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)