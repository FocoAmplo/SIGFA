from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.recommendation import RecommendationCreate
from ...schemas.recommendation import RecommendationResponse
from ...schemas.recommendation import RecommendationUpdate
from ...services.knowledge import RecommendationService

router = APIRouter(
    prefix="/knowledge/recommendations",
    tags=["Knowledge - Recommendations"],
)


@router.get("/", response_model=list[RecommendationResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return RecommendationService.get_all(db)


@router.get("/{id}", response_model=RecommendationResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    recommendation = RecommendationService.get_by_id(db, id)

    if not recommendation:
        raise HTTPException(status_code=404, detail="Recomendação não encontrada.")

    return recommendation


@router.post("/", response_model=RecommendationResponse)
def create(
    recommendation: RecommendationCreate,
    db: Session = Depends(get_db),
):
    return RecommendationService.create(db, recommendation)


@router.put("/{id}", response_model=RecommendationResponse)
def update(
    id: int,
    recommendation: RecommendationUpdate,
    db: Session = Depends(get_db),
):
    db_recommendation = RecommendationService.update(db, id, recommendation)

    if not db_recommendation:
        raise HTTPException(status_code=404, detail="Recomendação não encontrada.")

    return db_recommendation


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = RecommendationService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Recomendação não encontrada.")

    return {"deleted": deleted}
