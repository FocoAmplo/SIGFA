from sqlalchemy.orm import Session

from backend.app.models.answer import Answer
from backend.app.schemas.answer import AnswerCreate
from backend.app.schemas.answer import AnswerUpdate


class AnswerService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Answer)
            .order_by(Answer.id)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        answer_id: int,
    ):

        return (
            db.query(Answer)
            .filter(Answer.id == answer_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        answer: AnswerCreate,
    ):

        db_answer = Answer(**answer.model_dump())

        db.add(db_answer)

        db.commit()

        db.refresh(db_answer)

        return db_answer

    @staticmethod
    def update(
        db: Session,
        answer_id: int,
        answer: AnswerUpdate,
    ):

        db_answer = (
            db.query(Answer)
            .filter(Answer.id == answer_id)
            .first()
        )

        if not db_answer:
            return None

        update_data = answer.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_answer,
                key,
                value,
            )

        db.commit()

        db.refresh(db_answer)

        return db_answer

    @staticmethod
    def delete(
        db: Session,
        answer_id: int,
    ):

        db_answer = (
            db.query(Answer)
            .filter(Answer.id == answer_id)
            .first()
        )

        if not db_answer:
            return False

        db.delete(db_answer)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Answer)
            .filter(
                Answer.question_code.ilike(f"%{text}%")
            )
            .order_by(Answer.id)
            .all()
        )
