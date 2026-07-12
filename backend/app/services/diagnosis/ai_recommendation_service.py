from sqlalchemy.orm import Session

from app.models.ai_recommendation import AIRecommendation
from app.schemas.ai_recommendation import AIRecommendationCreate
from app.schemas.ai_recommendation import AIRecommendationUpdate


class AIRecommendationService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(AIRecommendation)
            .order_by(AIRecommendation.id)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        ai_recommendation_id: int,
    ):

        return (
            db.query(AIRecommendation)
            .filter(AIRecommendation.id == ai_recommendation_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        ai_recommendation: AIRecommendationCreate,
    ):

        db_ai_recommendation = AIRecommendation(**ai_recommendation.model_dump())

        db.add(db_ai_recommendation)

        db.commit()

        db.refresh(db_ai_recommendation)

        return db_ai_recommendation

    @staticmethod
    def update(
        db: Session,
        ai_recommendation_id: int,
        ai_recommendation: AIRecommendationUpdate,
    ):

        db_ai_recommendation = (
            db.query(AIRecommendation)
            .filter(AIRecommendation.id == ai_recommendation_id)
            .first()
        )

        if not db_ai_recommendation:
            return None

        update_data = ai_recommendation.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_ai_recommendation,
                key,
                value,
            )

        db.commit()

        db.refresh(db_ai_recommendation)

        return db_ai_recommendation

    @staticmethod
    def delete(
        db: Session,
        ai_recommendation_id: int,
    ):

        db_ai_recommendation = (
            db.query(AIRecommendation)
            .filter(AIRecommendation.id == ai_recommendation_id)
            .first()
        )

        if not db_ai_recommendation:
            return False

        db.delete(db_ai_recommendation)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(AIRecommendation)
            .filter(
                AIRecommendation.agent_code.ilike(f"%{text}%")
            )
            .order_by(AIRecommendation.id)
            .all()
        )
