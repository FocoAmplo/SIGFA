from sqlalchemy.orm import Session

from backend.app.models.omc import OMC
from backend.app.schemas.omc import OMCCreate
from backend.app.schemas.omc import OMCUpdate


class OMCService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(OMC)
            .order_by(OMC.title)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        omc_id: int,
    ):

        return (
            db.query(OMC)
            .filter(OMC.id == omc_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        omc: OMCCreate,
    ):

        db_omc = OMC(**omc.model_dump())

        db.add(db_omc)

        db.commit()

        db.refresh(db_omc)

        return db_omc

    @staticmethod
    def update(
        db: Session,
        omc_id: int,
        omc: OMCUpdate,
    ):

        db_omc = (
            db.query(OMC)
            .filter(OMC.id == omc_id)
            .first()
        )

        if not db_omc:
            return None

        update_data = omc.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_omc,
                key,
                value,
            )

        db.commit()

        db.refresh(db_omc)

        return db_omc

    @staticmethod
    def delete(
        db: Session,
        omc_id: int,
    ):

        db_omc = (
            db.query(OMC)
            .filter(OMC.id == omc_id)
            .first()
        )

        if not db_omc:
            return False

        db.delete(db_omc)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(OMC)
            .filter(
                OMC.title.ilike(f"%{text}%")
            )
            .order_by(OMC.title)
            .all()
        )

    @staticmethod
    def activate(
        db: Session,
        omc_id: int,
    ):

        db_omc = (
            db.query(OMC)
            .filter(OMC.id == omc_id)
            .first()
        )

        if not db_omc:
            return None

        db_omc.active = True

        db.commit()

        db.refresh(db_omc)

        return db_omc

    @staticmethod
    def deactivate(
        db: Session,
        omc_id: int,
    ):

        db_omc = (
            db.query(OMC)
            .filter(OMC.id == omc_id)
            .first()
        )

        if not db_omc:
            return None

        db_omc.active = False

        db.commit()

        db.refresh(db_omc)

        return db_omc