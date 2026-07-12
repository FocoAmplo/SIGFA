from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.ai_recommendation import AIRecommendationCreate
from ...schemas.ai_recommendation import AIRecommendationResponse
from ...schemas.ai_recommendation import AIRecommendationUpdate
from ...services.diagnosis import AIRecommendationService

router = APIRouter(
    prefix="/ai-recommendation",
    tags=["AI Recommendation"],
)


@router.get("/", response_model=list[AIRecommendationResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return AIRecommendationService.get_all(db)


@router.get("/{id}", response_model=AIRecommendationResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    ai_recommendation = AIRecommendationService.get_by_id(db, id)

    if not ai_recommendation:
        raise HTTPException(status_code=404, detail="AI recommendation not found.")

    return ai_recommendation


@router.post("/", response_model=AIRecommendationResponse)
def create(
    ai_recommendation: AIRecommendationCreate,
    db: Session = Depends(get_db),
):
    return AIRecommendationService.create(db, ai_recommendation)


@router.put("/{id}", response_model=AIRecommendationResponse)
def update(
    id: int,
    ai_recommendation: AIRecommendationUpdate,
    db: Session = Depends(get_db),
):
    db_ai_recommendation = AIRecommendationService.update(db, id, ai_recommendation)

    if not db_ai_recommendation:
        raise HTTPException(status_code=404, detail="AI recommendation not found.")

    return db_ai_recommendation


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = AIRecommendationService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="AI recommendation not found.")

    return {"deleted": deleted}
