from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PermissionBase(BaseModel):

    code: Optional[str] = None

    name: Optional[str] = None

    description: Optional[str] = None

    module: Optional[str] = None

    active: bool = True


class PermissionCreate(PermissionBase):
    pass


class PermissionUpdate(BaseModel):

    code: Optional[str] = None

    name: Optional[str] = None

    description: Optional[str] = None

    module: Optional[str] = None

    active: Optional[bool] = None


class PermissionResponse(PermissionBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)