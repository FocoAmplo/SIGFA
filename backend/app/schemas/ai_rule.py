from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AIRuleBase(BaseModel):

    code: Optional[str] = None

    title: Optional[str] = None

    condition: Optional[str] = None

    action: Optional[str] = None

    priority: Optional[int] = None

    active: bool = True


class AIRuleCreate(AIRuleBase):
    pass


class AIRuleUpdate(BaseModel):

    code: Optional[str] = None

    title: Optional[str] = None

    condition: Optional[str] = None

    action: Optional[str] = None

    priority: Optional[int] = None

    active: Optional[bool] = None


class AIRuleResponse(AIRuleBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)