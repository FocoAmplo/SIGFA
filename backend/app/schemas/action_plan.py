from datetime import date, datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ActionPlanBase(BaseModel):

    diagnosis_id: int

    recommendation_code: Optional[str] = None

    action_description: Optional[str] = None

    responsible: Optional[str] = None

    due_date: Optional[date] = None

    priority: Optional[str] = None

    status: str = "PENDING"

    progress: Decimal = Decimal("0.00")


class ActionPlanCreate(ActionPlanBase):
    pass


class ActionPlanUpdate(BaseModel):

    diagnosis_id: Optional[int] = None

    recommendation_code: Optional[str] = None

    action_description: Optional[str] = None

    responsible: Optional[str] = None

    due_date: Optional[date] = None

    priority: Optional[str] = None

    status: Optional[str] = None

    progress: Optional[Decimal] = None


class ActionPlanResponse(ActionPlanBase):

    id: int

    uuid: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)