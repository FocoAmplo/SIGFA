from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.evidence import EvidenceCreate
from ...schemas.evidence import EvidenceResponse
from ...schemas.evidence import EvidenceUpdate
from ...services.knowledge import EvidenceService

router = APIRouter(
    prefix="/knowledge/evidences",
    tags=["Knowledge - Evidences"],
)


@router.get("/", response_model=list[EvidenceResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return EvidenceService.get_all(db)


@router.get("/{id}", response_model=EvidenceResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    evidence = EvidenceService.get_by_id(db, id)

    if not evidence:
        raise HTTPException(status_code=404, detail="Evidência não encontrada.")

    return evidence


@router.post("/", response_model=EvidenceResponse)
def create(
    evidence: EvidenceCreate,
    db: Session = Depends(get_db),
):
    return EvidenceService.create(db, evidence)


@router.put("/{id}", response_model=EvidenceResponse)
def update(
    id: int,
    evidence: EvidenceUpdate,
    db: Session = Depends(get_db),
):
    db_evidence = EvidenceService.update(db, id, evidence)

    if not db_evidence:
        raise HTTPException(status_code=404, detail="Evidência não encontrada.")

    return db_evidence


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = EvidenceService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Evidência não encontrada.")

    return {"deleted": deleted}
