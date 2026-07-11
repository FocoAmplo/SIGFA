from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class FilterBase(BaseModel):

    dashboard_id: int

    filter_name: Optional[str] = None

    filter_type: Optional[str] = None

    source_table: Optional[str] = None

    source_field: Optional[str] = None

    active: bool = True


class FilterCreate(FilterBase):
    pass


class FilterUpdate(BaseModel):

    dashboard_id: Optional[int] = None

    filter_name: Optional[str] = None

    filter_type: Optional[str] = None

    source_table: Optional[str] = None

    source_field: Optional[str] = None

    active: Optional[bool] = None


class FilterResponse(FilterBase):

    id: int

    uuid: UUID

    model_config = ConfigDict(from_attributes=True)