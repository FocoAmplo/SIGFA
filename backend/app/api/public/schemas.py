from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import Field


class PublicLeadCreate(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=180,
    )

    email: EmailStr

    phone: Optional[str] = Field(
        default=None,
        max_length=30,
    )

    company_name: Optional[str] = Field(
        default=None,
        max_length=250,
    )

    segment: Optional[str] = Field(
        default=None,
        max_length=150,
    )

    city: Optional[str] = Field(
        default=None,
        max_length=120,
    )

    state: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=2,
    )

    employees: int = Field(
        default=0,
        ge=0,
    )

    monthly_revenue: Decimal = Field(
        default=Decimal("0"),
        ge=0,
    )

    main_problem: Optional[str] = None

    urgency: int = Field(
        default=1,
        ge=1,
        le=5,
    )

    investment_capacity: int = Field(
        default=1,
        ge=1,
        le=5,
    )

    source: str = Field(
        default="gpt_publico",
        max_length=80,
    )

    notes: Optional[str] = None


class PublicLeadResponse(BaseModel):

    id: int

    uuid: UUID

    name: str

    email: EmailStr

    company_name: Optional[str]

    segment: Optional[str]

    score: int

    classification: str

    status: str

    qualified: bool

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )


class PublicStatusResponse(BaseModel):

    status: str

    service: str

    version: str