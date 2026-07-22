from sqlalchemy.orm import Session

from backend.app.models.recommendation import Recommendation
from backend.app.schemas.recommendation import RecommendationCreate
from backend.app.schemas.recommendation import RecommendationUpdate


class RecommendationService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Recommendation)
            .order_by(Recommendation.title)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        recommendation_id: int,
    ):

        return (
            db.query(Recommendation)
            .filter(Recommendation.id == recommendation_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        recommendation: RecommendationCreate,
    ):

        db_recommendation = Recommendation(**recommendation.model_dump())

        db.add(db_recommendation)

        db.commit()

        db.refresh(db_recommendation)

        return db_recommendation

    @staticmethod
    def update(
        db: Session,
        recommendation_id: int,
        recommendation: RecommendationUpdate,
    ):

        db_recommendation = (
            db.query(Recommendation)
            .filter(Recommendation.id == recommendation_id)
            .first()
        )

        if not db_recommendation:
            return None

        update_data = recommendation.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_recommendation,
                key,
                value,
            )

        db.commit()

        db.refresh(db_recommendation)

        return db_recommendation

    @staticmethod
    def delete(
        db: Session,
        recommendation_id: int,
    ):

        db_recommendation = (
            db.query(Recommendation)
            .filter(Recommendation.id == recommendation_id)
            .first()
        )

        if not db_recommendation:
            return False

        db.delete(db_recommendation)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Recommendation)
            .filter(
                Recommendation.title.ilike(f"%{text}%")
            )
            .order_by(Recommendation.title)
            .all()
        )

    @staticmethod
    def activate(
        db: Session,
        recommendation_id: int,
    ):

        db_recommendation = (
            db.query(Recommendation)
            .filter(Recommendation.id == recommendation_id)
            .first()
        )

        if not db_recommendation:
            return None

        db_recommendation.active = True

        db.commit()

        db.refresh(db_recommendation)

        return db_recommendation

    @staticmethod
    def deactivate(
        db: Session,
        recommendation_id: int,
    ):

        db_recommendation = (
            db.query(Recommendation)
            .filter(Recommendation.id == recommendation_id)
            .first()
        )

        if not db_recommendation:
            return None

        db_recommendation.active = False

        db.commit()

        db.refresh(db_recommendation)

        return db_recommendation
