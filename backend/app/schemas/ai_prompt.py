from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AIPromptBase(BaseModel):

    agent_id: Optional[int] = None

    title: Optional[str] = None

    prompt: Optional[str] = None

    version: Optional[str] = None

    active: bool = True


class AIPromptCreate(AIPromptBase):
    pass


class AIPromptUpdate(BaseModel):

    agent_id: Optional[int] = None

    title: Optional[str] = None

    prompt: Optional[str] = None

    version: Optional[str] = None

    active: Optional[bool] = None


class AIPromptResponse(AIPromptBase):

    id: int

    uuid: UUID

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)