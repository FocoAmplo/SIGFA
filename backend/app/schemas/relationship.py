from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RelationshipBase(BaseModel):

    source_type: Optional[str] = None

    source_code: Optional[str] = None

    target_type: Optional[str] = None

    target_code: Optional[str] = None

    relationship_type: Optional[str] = None

    strength: Optional[Decimal] = None

    description: Optional[str] = None


class RelationshipCreate(RelationshipBase):
    pass


class RelationshipUpdate(BaseModel):

    source_type: Optional[str] = None

    source_code: Optional[str] = None

    target_type: Optional[str] = None

    target_code: Optional[str] = None

    relationship_type: Optional[str] = None

    strength: Optional[Decimal] = None

    description: Optional[str] = None


class RelationshipResponse(RelationshipBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)