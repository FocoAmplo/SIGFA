from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ChartBase(BaseModel):

    dashboard_id: int

    code: Optional[str] = None

    title: Optional[str] = None

    chart_type: Optional[str] = None

    sql_view: Optional[str] = None

    position: Optional[int] = None

    active: bool = True


class ChartCreate(ChartBase):
    pass


class ChartUpdate(BaseModel):

    dashboard_id: Optional[int] = None

    code: Optional[str] = None

    title: Optional[str] = None

    chart_type: Optional[str] = None

    sql_view: Optional[str] = None

    position: Optional[int] = None

    active: Optional[bool] = None


class ChartResponse(ChartBase):

    id: int

    uuid: UUID

    model_config = ConfigDict(from_attributes=True)