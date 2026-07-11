from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AIMemoryBase(BaseModel):

    agent_id: int

    context: Optional[str] = None

    source_type: Optional[str] = None

    source_code: Optional[str] = None

    confidence: Optional[Decimal] = None


class AIMemoryCreate(AIMemoryBase):
    pass


class AIMemoryUpdate(BaseModel):

    agent_id: Optional[int] = None

    context: Optional[str] = None

    source_type: Optional[str] = None

    source_code: Optional[str] = None

    confidence: Optional[Decimal] = None


class AIMemoryResponse(AIMemoryBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)