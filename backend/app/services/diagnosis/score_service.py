from sqlalchemy.orm import Session

from app.models.score import Score
from app.schemas.score import ScoreCreate
from app.schemas.score import ScoreUpdate


class ScoreService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Score)
            .order_by(Score.id)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        score_id: int,
    ):

        return (
            db.query(Score)
            .filter(Score.id == score_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        score: ScoreCreate,
    ):

        db_score = Score(**score.model_dump())

        db.add(db_score)

        db.commit()

        db.refresh(db_score)

        return db_score

    @staticmethod
    def update(
        db: Session,
        score_id: int,
        score: ScoreUpdate,
    ):

        db_score = (
            db.query(Score)
            .filter(Score.id == score_id)
            .first()
        )

        if not db_score:
            return None

        update_data = score.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_score,
                key,
                value,
            )

        db.commit()

        db.refresh(db_score)

        return db_score

    @staticmethod
    def delete(
        db: Session,
        score_id: int,
    ):

        db_score = (
            db.query(Score)
            .filter(Score.id == score_id)
            .first()
        )

        if not db_score:
            return False

        db.delete(db_score)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Score)
            .filter(
                Score.indicator_code.ilike(f"%{text}%")
            )
            .order_by(Score.id)
            .all()
        )
