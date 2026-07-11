from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RiskBase(BaseModel):

    omc_id: int

    code: str

    name: str

    description: Optional[str] = None

    probability: Optional[str] = None

    impact: Optional[str] = None

    severity: Optional[str] = None

    recommendation: Optional[str] = None

    keywords: Optional[str] = None

    embedding: Optional[str] = None

    version: str = "1.0"

    active: bool = True


class RiskCreate(RiskBase):
    pass


class RiskUpdate(BaseModel):

    omc_id: Optional[int] = None

    code: Optional[str] = None

    name: Optional[str] = None

    description: Optional[str] = None

    probability: Optional[str] = None

    impact: Optional[str] = None

    severity: Optional[str] = None

    recommendation: Optional[str] = None

    keywords: Optional[str] = None

    embedding: Optional[str] = None

    version: Optional[str] = None

    active: Optional[bool] = None


class RiskResponse(RiskBase):

    id: int

    uuid: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)