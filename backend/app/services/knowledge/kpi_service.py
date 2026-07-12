from sqlalchemy.orm import Session

from app.models.kpi import KPI
from app.schemas.kpi import KPICreate
from app.schemas.kpi import KPIUpdate


class KPIService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(KPI)
            .order_by(KPI.name)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        kpi_id: int,
    ):

        return (
            db.query(KPI)
            .filter(KPI.id == kpi_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        kpi: KPICreate,
    ):

        db_kpi = KPI(**kpi.model_dump())

        db.add(db_kpi)

        db.commit()

        db.refresh(db_kpi)

        return db_kpi

    @staticmethod
    def update(
        db: Session,
        kpi_id: int,
        kpi: KPIUpdate,
    ):

        db_kpi = (
            db.query(KPI)
            .filter(KPI.id == kpi_id)
            .first()
        )

        if not db_kpi:
            return None

        update_data = kpi.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_kpi,
                key,
                value,
            )

        db.commit()

        db.refresh(db_kpi)

        return db_kpi

    @staticmethod
    def delete(
        db: Session,
        kpi_id: int,
    ):

        db_kpi = (
            db.query(KPI)
            .filter(KPI.id == kpi_id)
            .first()
        )

        if not db_kpi:
            return False

        db.delete(db_kpi)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(KPI)
            .filter(
                KPI.name.ilike(f"%{text}%")
            )
            .order_by(KPI.name)
            .all()
        )

    @staticmethod
    def activate(
        db: Session,
        kpi_id: int,
    ):

        db_kpi = (
            db.query(KPI)
            .filter(KPI.id == kpi_id)
            .first()
        )

        if not db_kpi:
            return None

        db_kpi.active = True

        db.commit()

        db.refresh(db_kpi)

        return db_kpi

    @staticmethod
    def deactivate(
        db: Session,
        kpi_id: int,
    ):

        db_kpi = (
            db.query(KPI)
            .filter(KPI.id == kpi_id)
            .first()
        )

        if not db_kpi:
            return None

        db_kpi.active = False

        db.commit()

        db.refresh(db_kpi)

        return db_kpi
