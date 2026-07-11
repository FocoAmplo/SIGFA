from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ProfileBase(BaseModel):

    name: str

    description: Optional[str] = None

    active: bool = True


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(BaseModel):

    name: Optional[str] = None

    description: Optional[str] = None

    active: Optional[bool] = None


class ProfileResponse(ProfileBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)