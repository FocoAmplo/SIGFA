from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AnswerBase(BaseModel):

    diagnosis_id: int

    question_code: Optional[str] = None

    answer: Optional[str] = None

    score: Optional[Decimal] = None

    observation: Optional[str] = None

    evidence_file: Optional[str] = None


class AnswerCreate(AnswerBase):
    pass


class AnswerUpdate(BaseModel):

    diagnosis_id: Optional[int] = None

    question_code: Optional[str] = None

    answer: Optional[str] = None

    score: Optional[Decimal] = None

    observation: Optional[str] = None

    evidence_file: Optional[str] = None


class AnswerResponse(AnswerBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)