from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class OMCBase(BaseModel):

    code: str

    title: str

    category: Optional[str] = None

    subcategory: Optional[str] = None

    objective: Optional[str] = None

    version: str = "1.0"

    maturity_level: Decimal = Decimal("0.00")

    active: bool = True


class OMCCreate(OMCBase):
    pass


class OMCUpdate(BaseModel):

    code: Optional[str] = None

    title: Optional[str] = None

    category: Optional[str] = None

    subcategory: Optional[str] = None

    objective: Optional[str] = None

    version: Optional[str] = None

    maturity_level: Optional[Decimal] = None

    active: Optional[bool] = None


class OMCResponse(OMCBase):

    id: int

    uuid: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)