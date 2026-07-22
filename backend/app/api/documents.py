from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from backend.app.auth.dependencies import get_current_user
from backend.app.database.session import get_db
from backend.app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

service = DocumentService()


@router.post("/upload")
async def upload_document(
    files: list[UploadFile] = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    tenant_id = f"company_{current_user.company_id:07d}"
    documents = [
        await service.upload(file, db, current_user.company_id, current_user.id, tenant_id)
        for file in files
    ]
    db.commit()
    return {"documents": documents}
