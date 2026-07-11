from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AttachmentBase(BaseModel):

    diagnosis_id: int

    file_name: Optional[str] = None

    file_path: Optional[str] = None

    file_type: Optional[str] = None


class AttachmentCreate(AttachmentBase):
    pass


class AttachmentUpdate(BaseModel):

    diagnosis_id: Optional[int] = None

    file_name: Optional[str] = None

    file_path: Optional[str] = None

    file_type: Optional[str] = None


class AttachmentResponse(AttachmentBase):

    id: int

    uuid: UUID

    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)