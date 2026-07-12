from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.diagnosis import DiagnosisCreate
from ...schemas.diagnosis import DiagnosisResponse
from ...schemas.diagnosis import DiagnosisUpdate
from ...services.diagnosis import DiagnosisService

router = APIRouter(
    prefix="/diagnosis",
    tags=["Diagnosis"],
)


@router.get("/", response_model=list[DiagnosisResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return DiagnosisService.get_all(db)


@router.get("/{id}", response_model=DiagnosisResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    diagnosis = DiagnosisService.get_by_id(db, id)

    if not diagnosis:
        raise HTTPException(status_code=404, detail="Diagnosis not found.")

    return diagnosis


@router.post("/", response_model=DiagnosisResponse)
def create(
    diagnosis: DiagnosisCreate,
    db: Session = Depends(get_db),
):
    return DiagnosisService.create(db, diagnosis)


@router.put("/{id}", response_model=DiagnosisResponse)
def update(
    id: int,
    diagnosis: DiagnosisUpdate,
    db: Session = Depends(get_db),
):
    db_diagnosis = DiagnosisService.update(db, id, diagnosis)

    if not db_diagnosis:
        raise HTTPException(status_code=404, detail="Diagnosis not found.")

    return db_diagnosis


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = DiagnosisService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Diagnosis not found.")

    return {"deleted": deleted}
