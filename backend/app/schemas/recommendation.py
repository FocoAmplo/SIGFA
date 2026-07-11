from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RecommendationBase(BaseModel):

    omc_id: int

    code: str

    title: Optional[str] = None

    recommendation: Optional[str] = None

    priority: Optional[str] = None

    expected_result: Optional[str] = None

    estimated_time: Optional[str] = None

    keywords: Optional[str] = None

    embedding: Optional[str] = None

    version: str = "1.0"

    active: bool = True


class RecommendationCreate(RecommendationBase):
    pass


class RecommendationUpdate(BaseModel):

    omc_id: Optional[int] = None

    code: Optional[str] = None

    title: Optional[str] = None

    recommendation: Optional[str] = None

    priority: Optional[str] = None

    expected_result: Optional[str] = None

    estimated_time: Optional[str] = None

    keywords: Optional[str] = None

    embedding: Optional[str] = None

    version: Optional[str] = None

    active: Optional[bool] = None


class RecommendationResponse(RecommendationBase):

    id: int

    uuid: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)