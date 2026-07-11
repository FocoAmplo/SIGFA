from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class APILogBase(BaseModel):

    endpoint: Optional[str] = None

    method: Optional[str] = None

    status_code: Optional[int] = None

    execution_time_ms: Optional[Decimal] = None

    user_id: Optional[int] = None


class APILogCreate(APILogBase):
    pass


class APILogUpdate(BaseModel):

    endpoint: Optional[str] = None

    method: Optional[str] = None

    status_code: Optional[int] = None

    execution_time_ms: Optional[Decimal] = None

    user_id: Optional[int] = None


class APILogResponse(APILogBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)