from sqlalchemy.orm import Session

from backend.app.models.evidence import Evidence
from backend.app.schemas.evidence import EvidenceCreate
from backend.app.schemas.evidence import EvidenceUpdate


class EvidenceService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Evidence)
            .order_by(Evidence.name)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        evidence_id: int,
    ):

        return (
            db.query(Evidence)
            .filter(Evidence.id == evidence_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        evidence: EvidenceCreate,
    ):

        db_evidence = Evidence(**evidence.model_dump())

        db.add(db_evidence)

        db.commit()

        db.refresh(db_evidence)

        return db_evidence

    @staticmethod
    def update(
        db: Session,
        evidence_id: int,
        evidence: EvidenceUpdate,
    ):

        db_evidence = (
            db.query(Evidence)
            .filter(Evidence.id == evidence_id)
            .first()
        )

        if not db_evidence:
            return None

        update_data = evidence.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_evidence,
                key,
                value,
            )

        db.commit()

        db.refresh(db_evidence)

        return db_evidence

    @staticmethod
    def delete(
        db: Session,
        evidence_id: int,
    ):

        db_evidence = (
            db.query(Evidence)
            .filter(Evidence.id == evidence_id)
            .first()
        )

        if not db_evidence:
            return False

        db.delete(db_evidence)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Evidence)
            .filter(
                Evidence.name.ilike(f"%{text}%")
            )
            .order_by(Evidence.name)
            .all()
        )

    @staticmethod
    def activate(
        db: Session,
        evidence_id: int,
    ):

        db_evidence = (
            db.query(Evidence)
            .filter(Evidence.id == evidence_id)
            .first()
        )

        if not db_evidence:
            return None

        db_evidence.active = True

        db.commit()

        db.refresh(db_evidence)

        return db_evidence

    @staticmethod
    def deactivate(
        db: Session,
        evidence_id: int,
    ):

        db_evidence = (
            db.query(Evidence)
            .filter(Evidence.id == evidence_id)
            .first()
        )

        if not db_evidence:
            return None

        db_evidence.active = False

        db.commit()

        db.refresh(db_evidence)

        return db_evidence
