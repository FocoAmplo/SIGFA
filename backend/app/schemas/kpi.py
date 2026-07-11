from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class KPIBase(BaseModel):

    omc_id: int

    code: str

    name: str

    description: Optional[str] = None

    formula: Optional[str] = None

    unit: Optional[str] = None

    target_value: Optional[Decimal] = None

    warning_value: Optional[Decimal] = None

    critical_value: Optional[Decimal] = None

    frequency: Optional[str] = None

    keywords: Optional[str] = None

    embedding: Optional[str] = None

    version: str = "1.0"

    active: bool = True


class KPICreate(KPIBase):
    pass


class KPIUpdate(BaseModel):

    omc_id: Optional[int] = None

    code: Optional[str] = None

    name: Optional[str] = None

    description: Optional[str] = None

    formula: Optional[str] = None

    unit: Optional[str] = None

    target_value: Optional[Decimal] = None

    warning_value: Optional[Decimal] = None

    critical_value: Optional[Decimal] = None

    frequency: Optional[str] = None

    keywords: Optional[str] = None

    embedding: Optional[str] = None

    version: Optional[str] = None

    active: Optional[bool] = None


class KPIResponse(KPIBase):

    id: int

    uuid: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)