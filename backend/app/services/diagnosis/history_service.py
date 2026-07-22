from sqlalchemy.orm import Session

from backend.app.models.history import History
from backend.app.schemas.history import HistoryCreate
from backend.app.schemas.history import HistoryUpdate


class HistoryService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(History)
            .order_by(History.id)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        history_id: int,
    ):

        return (
            db.query(History)
            .filter(History.id == history_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        history: HistoryCreate,
    ):

        db_history = History(**history.model_dump())

        db.add(db_history)

        db.commit()

        db.refresh(db_history)

        return db_history

    @staticmethod
    def update(
        db: Session,
        history_id: int,
        history: HistoryUpdate,
    ):

        db_history = (
            db.query(History)
            .filter(History.id == history_id)
            .first()
        )

        if not db_history:
            return None

        update_data = history.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_history,
                key,
                value,
            )

        db.commit()

        db.refresh(db_history)

        return db_history

    @staticmethod
    def delete(
        db: Session,
        history_id: int,
    ):

        db_history = (
            db.query(History)
            .filter(History.id == history_id)
            .first()
        )

        if not db_history:
            return False

        db.delete(db_history)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(History)
            .filter(
                History.description.ilike(f"%{text}%")
            )
            .order_by(History.id)
            .all()
        )
