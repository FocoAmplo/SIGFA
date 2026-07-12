from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.schemas.profile import ProfileCreate
from app.schemas.profile import ProfileUpdate


class ProfileService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Profile)
            .order_by(Profile.name)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        profile_id: int,
    ):

        return (
            db.query(Profile)
            .filter(Profile.id == profile_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        profile: ProfileCreate,
    ):

        db_profile = Profile(**profile.model_dump())

        db.add(db_profile)

        db.commit()

        db.refresh(db_profile)

        return db_profile

    @staticmethod
    def update(
        db: Session,
        profile_id: int,
        profile: ProfileUpdate,
    ):

        db_profile = (
            db.query(Profile)
            .filter(Profile.id == profile_id)
            .first()
        )

        if not db_profile:
            return None

        update_data = profile.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_profile,
                key,
                value,
            )

        db.commit()

        db.refresh(db_profile)

        return db_profile

    @staticmethod
    def delete(
        db: Session,
        profile_id: int,
    ):

        db_profile = (
            db.query(Profile)
            .filter(Profile.id == profile_id)
            .first()
        )

        if not db_profile:
            return False

        db.delete(db_profile)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Profile)
            .filter(
                Profile.name.ilike(f"%{text}%")
            )
            .order_by(Profile.name)
            .all()
        )