from sqlalchemy.orm import Session

from backend.app.models.diagnosis import Diagnosis
from backend.app.schemas.diagnosis import DiagnosisCreate
from backend.app.schemas.diagnosis import DiagnosisUpdate


class DiagnosisService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Diagnosis)
            .order_by(Diagnosis.id)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        diagnosis_id: int,
    ):

        return (
            db.query(Diagnosis)
            .filter(Diagnosis.id == diagnosis_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        diagnosis: DiagnosisCreate,
    ):

        db_diagnosis = Diagnosis(**diagnosis.model_dump())

        db.add(db_diagnosis)

        db.commit()

        db.refresh(db_diagnosis)

        return db_diagnosis

    @staticmethod
    def update(
        db: Session,
        diagnosis_id: int,
        diagnosis: DiagnosisUpdate,
    ):

        db_diagnosis = (
            db.query(Diagnosis)
            .filter(Diagnosis.id == diagnosis_id)
            .first()
        )

        if not db_diagnosis:
            return None

        update_data = diagnosis.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_diagnosis,
                key,
                value,
            )

        db.commit()

        db.refresh(db_diagnosis)

        return db_diagnosis

    @staticmethod
    def delete(
        db: Session,
        diagnosis_id: int,
    ):

        db_diagnosis = (
            db.query(Diagnosis)
            .filter(Diagnosis.id == diagnosis_id)
            .first()
        )

        if not db_diagnosis:
            return False

        db.delete(db_diagnosis)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Diagnosis)
            .filter(
                Diagnosis.title.ilike(f"%{text}%")
            )
            .order_by(Diagnosis.id)
            .all()
        )
