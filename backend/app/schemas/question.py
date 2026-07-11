from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class QuestionBase(BaseModel):

    omc_id: int

    code: str

    question: str

    question_type: Optional[str] = None

    weight: Optional[Decimal] = None

    required_evidence: bool = False

    help_text: Optional[str] = None

    keywords: Optional[str] = None

    embedding: Optional[str] = None

    version: str = "1.0"

    active: bool = True


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(BaseModel):

    omc_id: Optional[int] = None

    code: Optional[str] = None

    question: Optional[str] = None

    question_type: Optional[str] = None

    weight: Optional[Decimal] = None

    required_evidence: Optional[bool] = None

    help_text: Optional[str] = None

    keywords: Optional[str] = None

    embedding: Optional[str] = None

    version: Optional[str] = None

    active: Optional[bool] = None


class QuestionResponse(QuestionBase):

    id: int

    uuid: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)