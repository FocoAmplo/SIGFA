from datetime import datetime

from pydantic import BaseModel


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RefreshResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_at: datetime
