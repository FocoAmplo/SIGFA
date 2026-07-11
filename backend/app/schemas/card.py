from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CardBase(BaseModel):

    dashboard_id: int

    code: Optional[str] = None

    title: Optional[str] = None

    metric_code: Optional[str] = None

    icon: Optional[str] = None

    color: Optional[str] = None

    position: Optional[int] = None

    active: bool = True


class CardCreate(CardBase):
    pass


class CardUpdate(BaseModel):

    dashboard_id: Optional[int] = None

    code: Optional[str] = None

    title: Optional[str] = None

    metric_code: Optional[str] = None

    icon: Optional[str] = None

    color: Optional[str] = None

    position: Optional[int] = None

    active: Optional[bool] = None


class CardResponse(CardBase):

    id: int

    uuid: UUID

    model_config = ConfigDict(from_attributes=True)