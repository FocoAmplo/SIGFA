from sqlalchemy.orm import Session

from app.models.question import Question
from app.schemas.question import QuestionCreate
from app.schemas.question import QuestionUpdate


class QuestionService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Question)
            .order_by(Question.question)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        question_id: int,
    ):

        return (
            db.query(Question)
            .filter(Question.id == question_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        question: QuestionCreate,
    ):

        db_question = Question(**question.model_dump())

        db.add(db_question)

        db.commit()

        db.refresh(db_question)

        return db_question

    @staticmethod
    def update(
        db: Session,
        question_id: int,
        question: QuestionUpdate,
    ):

        db_question = (
            db.query(Question)
            .filter(Question.id == question_id)
            .first()
        )

        if not db_question:
            return None

        update_data = question.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_question,
                key,
                value,
            )

        db.commit()

        db.refresh(db_question)

        return db_question

    @staticmethod
    def delete(
        db: Session,
        question_id: int,
    ):

        db_question = (
            db.query(Question)
            .filter(Question.id == question_id)
            .first()
        )

        if not db_question:
            return False

        db.delete(db_question)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Question)
            .filter(
                Question.question.ilike(f"%{text}%")
            )
            .order_by(Question.question)
            .all()
        )

    @staticmethod
    def activate(
        db: Session,
        question_id: int,
    ):

        db_question = (
            db.query(Question)
            .filter(Question.id == question_id)
            .first()
        )

        if not db_question:
            return None

        db_question.active = True

        db.commit()

        db.refresh(db_question)

        return db_question

    @staticmethod
    def deactivate(
        db: Session,
        question_id: int,
    ):

        db_question = (
            db.query(Question)
            .filter(Question.id == question_id)
            .first()
        )

        if not db_question:
            return None

        db_question.active = False

        db.commit()

        db.refresh(db_question)

        return db_question
