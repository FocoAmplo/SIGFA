from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class NotificationBase(BaseModel):

    company_id: Optional[int] = None

    title: Optional[str] = None

    message: Optional[str] = None

    notification_type: Optional[str] = None

    readed: bool = False


class NotificationCreate(NotificationBase):
    pass


class NotificationUpdate(BaseModel):

    company_id: Optional[int] = None

    title: Optional[str] = None

    message: Optional[str] = None

    notification_type: Optional[str] = None

    readed: Optional[bool] = None


class NotificationResponse(NotificationBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)