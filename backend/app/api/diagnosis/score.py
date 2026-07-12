from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.score import ScoreCreate
from ...schemas.score import ScoreResponse
from ...schemas.score import ScoreUpdate
from ...services.diagnosis import ScoreService

router = APIRouter(
    prefix="/score",
    tags=["Score"],
)


@router.get("/", response_model=list[ScoreResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return ScoreService.get_all(db)


@router.get("/{id}", response_model=ScoreResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    score = ScoreService.get_by_id(db, id)

    if not score:
        raise HTTPException(status_code=404, detail="Score not found.")

    return score


@router.post("/", response_model=ScoreResponse)
def create(
    score: ScoreCreate,
    db: Session = Depends(get_db),
):
    return ScoreService.create(db, score)


@router.put("/{id}", response_model=ScoreResponse)
def update(
    id: int,
    score: ScoreUpdate,
    db: Session = Depends(get_db),
):
    db_score = ScoreService.update(db, id, score)

    if not db_score:
        raise HTTPException(status_code=404, detail="Score not found.")

    return db_score


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = ScoreService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Score not found.")

    return {"deleted": deleted}
