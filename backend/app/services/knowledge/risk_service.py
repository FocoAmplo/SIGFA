from sqlalchemy.orm import Session

from backend.app.models.risk import Risk
from backend.app.schemas.risk import RiskCreate
from backend.app.schemas.risk import RiskUpdate


class RiskService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Risk)
            .order_by(Risk.name)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        risk_id: int,
    ):

        return (
            db.query(Risk)
            .filter(Risk.id == risk_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        risk: RiskCreate,
    ):

        db_risk = Risk(**risk.model_dump())

        db.add(db_risk)

        db.commit()

        db.refresh(db_risk)

        return db_risk

    @staticmethod
    def update(
        db: Session,
        risk_id: int,
        risk: RiskUpdate,
    ):

        db_risk = (
            db.query(Risk)
            .filter(Risk.id == risk_id)
            .first()
        )

        if not db_risk:
            return None

        update_data = risk.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_risk,
                key,
                value,
            )

        db.commit()

        db.refresh(db_risk)

        return db_risk

    @staticmethod
    def delete(
        db: Session,
        risk_id: int,
    ):

        db_risk = (
            db.query(Risk)
            .filter(Risk.id == risk_id)
            .first()
        )

        if not db_risk:
            return False

        db.delete(db_risk)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Risk)
            .filter(
                Risk.name.ilike(f"%{text}%")
            )
            .order_by(Risk.name)
            .all()
        )

    @staticmethod
    def activate(
        db: Session,
        risk_id: int,
    ):

        db_risk = (
            db.query(Risk)
            .filter(Risk.id == risk_id)
            .first()
        )

        if not db_risk:
            return None

        db_risk.active = True

        db.commit()

        db.refresh(db_risk)

        return db_risk

    @staticmethod
    def deactivate(
        db: Session,
        risk_id: int,
    ):

        db_risk = (
            db.query(Risk)
            .filter(Risk.id == risk_id)
            .first()
        )

        if not db_risk:
            return None

        db_risk.active = False

        db.commit()

        db.refresh(db_risk)

        return db_risk
