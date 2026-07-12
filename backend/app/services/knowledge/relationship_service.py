from sqlalchemy.orm import Session

from app.models.relationship import Relationship
from app.schemas.relationship import RelationshipCreate
from app.schemas.relationship import RelationshipUpdate


class RelationshipService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Relationship)
            .order_by(Relationship.source_code)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        relationship_id: int,
    ):

        return (
            db.query(Relationship)
            .filter(Relationship.id == relationship_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        relationship: RelationshipCreate,
    ):

        db_relationship = Relationship(**relationship.model_dump())

        db.add(db_relationship)

        db.commit()

        db.refresh(db_relationship)

        return db_relationship

    @staticmethod
    def update(
        db: Session,
        relationship_id: int,
        relationship: RelationshipUpdate,
    ):

        db_relationship = (
            db.query(Relationship)
            .filter(Relationship.id == relationship_id)
            .first()
        )

        if not db_relationship:
            return None

        update_data = relationship.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_relationship,
                key,
                value,
            )

        db.commit()

        db.refresh(db_relationship)

        return db_relationship

    @staticmethod
    def delete(
        db: Session,
        relationship_id: int,
    ):

        db_relationship = (
            db.query(Relationship)
            .filter(Relationship.id == relationship_id)
            .first()
        )

        if not db_relationship:
            return False

        db.delete(db_relationship)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Relationship)
            .filter(
                Relationship.source_code.ilike(f"%{text}%")
            )
            .order_by(Relationship.source_code)
            .all()
        )

    @staticmethod
    def activate(
        db: Session,
        relationship_id: int,
    ):

        db_relationship = (
            db.query(Relationship)
            .filter(Relationship.id == relationship_id)
            .first()
        )

        if not db_relationship:
            return None

        db_relationship.active = True

        db.commit()

        db.refresh(db_relationship)

        return db_relationship

    @staticmethod
    def deactivate(
        db: Session,
        relationship_id: int,
    ):

        db_relationship = (
            db.query(Relationship)
            .filter(Relationship.id == relationship_id)
            .first()
        )

        if not db_relationship:
            return None

        db_relationship.active = False

        db.commit()

        db.refresh(db_relationship)

        return db_relationship
