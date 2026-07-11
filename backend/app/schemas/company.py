from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CompanyBase(BaseModel):

    corporate_name: str

    trade_name: Optional[str] = None

    cnpj: Optional[str] = None

    state_registration: Optional[str] = None

    municipal_registration: Optional[str] = None

    segment: Optional[str] = None

    employees: int = 0

    city: Optional[str] = None

    state: Optional[str] = None

    country: str = "Brasil"

    phone: Optional[str] = None

    email: Optional[str] = None

    website: Optional[str] = None

    active: bool = True


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(BaseModel):

    corporate_name: Optional[str] = None

    trade_name: Optional[str] = None

    cnpj: Optional[str] = None

    state_registration: Optional[str] = None

    municipal_registration: Optional[str] = None

    segment: Optional[str] = None

    employees: Optional[int] = None

    city: Optional[str] = None

    state: Optional[str] = None

    country: Optional[str] = None

    phone: Optional[str] = None

    email: Optional[str] = None

    website: Optional[str] = None

    active: Optional[bool] = None


class CompanyResponse(CompanyBase):

    id: int

    uuid: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)