from sqlalchemy.orm import Session

from app.models.concept import Concept
from app.schemas.concept import ConceptCreate
from app.schemas.concept import ConceptUpdate


class ConceptService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Concept)
            .order_by(Concept.name)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        concept_id: int,
    ):

        return (
            db.query(Concept)
            .filter(Concept.id == concept_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        concept: ConceptCreate,
    ):

        db_concept = Concept(**concept.model_dump())

        db.add(db_concept)

        db.commit()

        db.refresh(db_concept)

        return db_concept

    @staticmethod
    def update(
        db: Session,
        concept_id: int,
        concept: ConceptUpdate,
    ):

        db_concept = (
            db.query(Concept)
            .filter(Concept.id == concept_id)
            .first()
        )

        if not db_concept:
            return None

        update_data = concept.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_concept,
                key,
                value,
            )

        db.commit()

        db.refresh(db_concept)

        return db_concept

    @staticmethod
    def delete(
        db: Session,
        concept_id: int,
    ):

        db_concept = (
            db.query(Concept)
            .filter(Concept.id == concept_id)
            .first()
        )

        if not db_concept:
            return False

        db.delete(db_concept)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Concept)
            .filter(
                Concept.name.ilike(f"%{text}%")
            )
            .order_by(Concept.name)
            .all()
        )

    @staticmethod
    def activate(
        db: Session,
        concept_id: int,
    ):

        db_concept = (
            db.query(Concept)
            .filter(Concept.id == concept_id)
            .first()
        )

        if not db_concept:
            return None

        db_concept.active = True

        db.commit()

        db.refresh(db_concept)

        return db_concept

    @staticmethod
    def deactivate(
        db: Session,
        concept_id: int,
    ):

        db_concept = (
            db.query(Concept)
            .filter(Concept.id == concept_id)
            .first()
        )

        if not db_concept:
            return None

        db_concept.active = False

        db.commit()

        db.refresh(db_concept)

        return db_concept
