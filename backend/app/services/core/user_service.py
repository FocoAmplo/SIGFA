from sqlalchemy.orm import Session

from backend.app.models.user import User
from backend.app.schemas.user import UserCreate
from backend.app.schemas.user import UserUpdate


class UserService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(User)
            .order_by(User.name)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        user_id: int,
    ):

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        user: UserCreate,
    ):

        db_user = User(**user.model_dump())

        db.add(db_user)

        db.commit()

        db.refresh(db_user)

        return db_user

    @staticmethod
    def update(
        db: Session,
        user_id: int,
        user: UserUpdate,
    ):

        db_user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not db_user:
            return None

        update_data = user.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_user,
                key,
                value,
            )

        db.commit()

        db.refresh(db_user)

        return db_user

    @staticmethod
    def delete(
        db: Session,
        user_id: int,
    ):

        db_user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not db_user:
            return False

        db.delete(db_user)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(User)
            .filter(
                User.name.ilike(f"%{text}%")
            )
            .order_by(User.name)
            .all()
        )