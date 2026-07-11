from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DashboardBase(BaseModel):

    code: Optional[str] = None

    name: Optional[str] = None

    description: Optional[str] = None

    active: bool = True


class DashboardCreate(DashboardBase):
    pass


class DashboardUpdate(BaseModel):

    code: Optional[str] = None

    name: Optional[str] = None

    description: Optional[str] = None

    active: Optional[bool] = None


class DashboardResponse(DashboardBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)