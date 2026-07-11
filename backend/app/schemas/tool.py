from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ToolBase(BaseModel):

    omc_id: int

    code: str

    name: Optional[str] = None

    description: Optional[str] = None

    application: Optional[str] = None

    keywords: Optional[str] = None

    embedding: Optional[str] = None

    version: str = "1.0"

    active: bool = True


class ToolCreate(ToolBase):
    pass


class ToolUpdate(BaseModel):

    omc_id: Optional[int] = None

    code: Optional[str] = None

    name: Optional[str] = None

    description: Optional[str] = None

    application: Optional[str] = None

    keywords: Optional[str] = None

    embedding: Optional[str] = None

    version: Optional[str] = None

    active: Optional[bool] = None


class ToolResponse(ToolBase):

    id: int

    uuid: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)