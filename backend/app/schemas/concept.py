from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ConceptBase(BaseModel):

    omc_id: int

    code: str

    name: str

    definition: Optional[str] = None

    objective: Optional[str] = None

    process: Optional[str] = None

    area: Optional[str] = None

    domain: Optional[str] = None

    keywords: Optional[str] = None

    embedding: Optional[str] = None

    version: str = "1.0"

    active: bool = True


class ConceptCreate(ConceptBase):
    pass


class ConceptUpdate(BaseModel):

    omc_id: Optional[int] = None

    code: Optional[str] = None

    name: Optional[str] = None

    definition: Optional[str] = None

    objective: Optional[str] = None

    process: Optional[str] = None

    area: Optional[str] = None

    domain: Optional[str] = None

    keywords: Optional[str] = None

    embedding: Optional[str] = None

    version: Optional[str] = None

    active: Optional[bool] = None


class ConceptResponse(ConceptBase):

    id: int

    uuid: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)