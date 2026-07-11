from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DiagnosisBase(BaseModel):

    company_id: int

    title: Optional[str] = None

    omc_code: Optional[str] = None

    status: str = "OPEN"

    score: Optional[Decimal] = None

    maturity_level: Optional[Decimal] = None

    risk_level: Optional[str] = None

    started_at: Optional[datetime] = None

    finished_at: Optional[datetime] = None


class DiagnosisCreate(DiagnosisBase):
    pass


class DiagnosisUpdate(BaseModel):

    company_id: Optional[int] = None

    title: Optional[str] = None

    omc_code: Optional[str] = None

    status: Optional[str] = None

    score: Optional[Decimal] = None

    maturity_level: Optional[Decimal] = None

    risk_level: Optional[str] = None

    started_at: Optional[datetime] = None

    finished_at: Optional[datetime] = None


class DiagnosisResponse(DiagnosisBase):

    id: int

    uuid: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)