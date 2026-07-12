from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.attachment import AttachmentCreate
from ...schemas.attachment import AttachmentResponse
from ...schemas.attachment import AttachmentUpdate
from ...services.diagnosis import AttachmentService

router = APIRouter(
    prefix="/attachment",
    tags=["Attachment"],
)


@router.get("/", response_model=list[AttachmentResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return AttachmentService.get_all(db)


@router.get("/{id}", response_model=AttachmentResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    attachment = AttachmentService.get_by_id(db, id)

    if not attachment:
        raise HTTPException(status_code=404, detail="Attachment not found.")

    return attachment


@router.post("/", response_model=AttachmentResponse)
def create(
    attachment: AttachmentCreate,
    db: Session = Depends(get_db),
):
    return AttachmentService.create(db, attachment)


@router.put("/{id}", response_model=AttachmentResponse)
def update(
    id: int,
    attachment: AttachmentUpdate,
    db: Session = Depends(get_db),
):
    db_attachment = AttachmentService.update(db, id, attachment)

    if not db_attachment:
        raise HTTPException(status_code=404, detail="Attachment not found.")

    return db_attachment


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = AttachmentService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Attachment not found.")

    return {"deleted": deleted}
