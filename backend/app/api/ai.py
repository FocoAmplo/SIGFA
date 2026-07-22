from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.orm import Session

from backend.app.auth.dependencies import get_current_user
from backend.app.database.session import get_db
from backend.app.services.ai_service import ai_service

router = APIRouter(prefix="/ai", tags=["Artificial Intelligence"])


@router.post("/chat")
async def chat(
    prompt: str = Form(default=""),
    files: list[UploadFile] = File(default_factory=list),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return await ai_service.chat(
        prompt=prompt,
        files=files,
        db=db,
        user=current_user,
    )
