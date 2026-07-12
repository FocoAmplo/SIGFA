from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.concept import ConceptCreate
from ...schemas.concept import ConceptResponse
from ...schemas.concept import ConceptUpdate
from ...services.knowledge import ConceptService

router = APIRouter(
    prefix="/knowledge/concepts",
    tags=["Knowledge - Concepts"],
)


@router.get("/", response_model=list[ConceptResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return ConceptService.get_all(db)


@router.get("/{id}", response_model=ConceptResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    concept = ConceptService.get_by_id(db, id)

    if not concept:
        raise HTTPException(status_code=404, detail="Conceito não encontrado.")

    return concept


@router.post("/", response_model=ConceptResponse)
def create(
    concept: ConceptCreate,
    db: Session = Depends(get_db),
):
    return ConceptService.create(db, concept)


@router.put("/{id}", response_model=ConceptResponse)
def update(
    id: int,
    concept: ConceptUpdate,
    db: Session = Depends(get_db),
):
    db_concept = ConceptService.update(db, id, concept)

    if not db_concept:
        raise HTTPException(status_code=404, detail="Conceito não encontrado.")

    return db_concept


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = ConceptService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Conceito não encontrado.")

    return {"deleted": deleted}
