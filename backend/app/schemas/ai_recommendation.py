from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AIRecommendationBase(BaseModel):

    diagnosis_id: int

    agent_code: Optional[str] = None

    recommendation: Optional[str] = None

    confidence: Optional[Decimal] = None

    accepted: Optional[bool] = None


class AIRecommendationCreate(AIRecommendationBase):
    pass


class AIRecommendationUpdate(BaseModel):

    diagnosis_id: Optional[int] = None

    agent_code: Optional[str] = None

    recommendation: Optional[str] = None

    confidence: Optional[Decimal] = None

    accepted: Optional[bool] = None


class AIRecommendationResponse(AIRecommendationBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)