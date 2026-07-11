from pydantic import BaseModel
from typing import Literal


class ExternalLoginRequest(BaseModel):
    provider: Literal["google", "microsoft", "github"]
    email: str
    name: str | None = None
    avatar_url: str | None = None
