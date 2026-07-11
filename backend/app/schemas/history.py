from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class HistoryBase(BaseModel):

    diagnosis_id: int

    event_type: Optional[str] = None

    description: Optional[str] = None

    user_name: Optional[str] = None


class HistoryCreate(HistoryBase):
    pass


class HistoryUpdate(BaseModel):

    diagnosis_id: Optional[int] = None

    event_type: Optional[str] = None

    description: Optional[str] = None

    user_name: Optional[str] = None


class HistoryResponse(HistoryBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)