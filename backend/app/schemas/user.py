from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):

    company_id: int

    profile_id: Optional[int] = None

    name: str

    email: EmailStr

    phone: Optional[str] = None

    avatar: Optional[str] = None

    active: bool = True


class UserCreate(UserBase):

    password: str


class UserUpdate(BaseModel):

    profile_id: Optional[int] = None

    name: Optional[str] = None

    email: Optional[EmailStr] = None

    phone: Optional[str] = None

    avatar: Optional[str] = None

    active: Optional[bool] = None


class UserResponse(UserBase):

    id: int

    uuid: UUID

    last_login: Optional[datetime]

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)