from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AuditLogBase(BaseModel):

    user_id: Optional[int] = None

    module: Optional[str] = None

    action: Optional[str] = None

    table_name: Optional[str] = None

    record_id: Optional[int] = None

    old_data: Optional[dict[str, Any]] = None

    new_data: Optional[dict[str, Any]] = None

    ip_address: Optional[str] = None


class AuditLogCreate(AuditLogBase):
    pass


class AuditLogUpdate(BaseModel):

    user_id: Optional[int] = None

    module: Optional[str] = None

    action: Optional[str] = None

    table_name: Optional[str] = None

    record_id: Optional[int] = None

    old_data: Optional[dict[str, Any]] = None

    new_data: Optional[dict[str, Any]] = None

    ip_address: Optional[str] = None


class AuditLogResponse(AuditLogBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)