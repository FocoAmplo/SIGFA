from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class DocumentBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None


class DocumentCreate(DocumentBase):
    pass


class DocumentRead(DocumentBase):
    id: int
    filename: str
    filepath: str
    empresa_id: int
    uploaded_by: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)