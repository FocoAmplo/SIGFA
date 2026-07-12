from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.relationship import RelationshipCreate
from ...schemas.relationship import RelationshipResponse
from ...schemas.relationship import RelationshipUpdate
from ...services.knowledge import RelationshipService

router = APIRouter(
    prefix="/knowledge/relationships",
    tags=["Knowledge - Relationships"],
)


@router.get("/", response_model=list[RelationshipResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return RelationshipService.get_all(db)


@router.get("/{id}", response_model=RelationshipResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    relationship = RelationshipService.get_by_id(db, id)

    if not relationship:
        raise HTTPException(status_code=404, detail="Relacionamento não encontrado.")

    return relationship


@router.post("/", response_model=RelationshipResponse)
def create(
    relationship: RelationshipCreate,
    db: Session = Depends(get_db),
):
    return RelationshipService.create(db, relationship)


@router.put("/{id}", response_model=RelationshipResponse)
def update(
    id: int,
    relationship: RelationshipUpdate,
    db: Session = Depends(get_db),
):
    db_relationship = RelationshipService.update(db, id, relationship)

    if not db_relationship:
        raise HTTPException(status_code=404, detail="Relacionamento não encontrado.")

    return db_relationship


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = RelationshipService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Relacionamento não encontrado.")

    return {"deleted": deleted}
