from sqlalchemy.orm import Session

from app.models.method import Method
from app.schemas.method import MethodCreate
from app.schemas.method import MethodUpdate


class MethodService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Method)
            .order_by(Method.name)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        method_id: int,
    ):

        return (
            db.query(Method)
            .filter(Method.id == method_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        method: MethodCreate,
    ):

        db_method = Method(**method.model_dump())

        db.add(db_method)

        db.commit()

        db.refresh(db_method)

        return db_method

    @staticmethod
    def update(
        db: Session,
        method_id: int,
        method: MethodUpdate,
    ):

        db_method = (
            db.query(Method)
            .filter(Method.id == method_id)
            .first()
        )

        if not db_method:
            return None

        update_data = method.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_method,
                key,
                value,
            )

        db.commit()

        db.refresh(db_method)

        return db_method

    @staticmethod
    def delete(
        db: Session,
        method_id: int,
    ):

        db_method = (
            db.query(Method)
            .filter(Method.id == method_id)
            .first()
        )

        if not db_method:
            return False

        db.delete(db_method)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Method)
            .filter(
                Method.name.ilike(f"%{text}%")
            )
            .order_by(Method.name)
            .all()
        )

    @staticmethod
    def activate(
        db: Session,
        method_id: int,
    ):

        db_method = (
            db.query(Method)
            .filter(Method.id == method_id)
            .first()
        )

        if not db_method:
            return None

        db_method.active = True

        db.commit()

        db.refresh(db_method)

        return db_method

    @staticmethod
    def deactivate(
        db: Session,
        method_id: int,
    ):

        db_method = (
            db.query(Method)
            .filter(Method.id == method_id)
            .first()
        )

        if not db_method:
            return None

        db_method.active = False

        db.commit()

        db.refresh(db_method)

        return db_method
