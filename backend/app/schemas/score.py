from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ScoreBase(BaseModel):

    diagnosis_id: int

    indicator_code: Optional[str] = None

    value: Optional[Decimal] = None


class ScoreCreate(ScoreBase):
    pass


class ScoreUpdate(BaseModel):

    diagnosis_id: Optional[int] = None

    indicator_code: Optional[str] = None

    value: Optional[Decimal] = None


class ScoreResponse(ScoreBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)