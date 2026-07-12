from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas.company import CompanyCreate
from app.schemas.company import CompanyUpdate


class CompanyService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Company)
            .order_by(Company.corporate_name)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        company_id: int,
    ):

        return (
            db.query(Company)
            .filter(Company.id == company_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        company: CompanyCreate,
    ):

        db_company = Company(**company.model_dump())

        db.add(db_company)

        db.commit()

        db.refresh(db_company)

        return db_company

    @staticmethod
    def update(
        db: Session,
        company_id: int,
        company: CompanyUpdate,
    ):

        db_company = (
            db.query(Company)
            .filter(Company.id == company_id)
            .first()
        )

        if not db_company:
            return None

        update_data = company.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_company,
                key,
                value,
            )

        db.commit()

        db.refresh(db_company)

        return db_company

    @staticmethod
    def delete(
        db: Session,
        company_id: int,
    ):

        db_company = (
            db.query(Company)
            .filter(Company.id == company_id)
            .first()
        )

        if not db_company:
            return False

        db.delete(db_company)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Company)
            .filter(
                Company.corporate_name.ilike(f"%{text}%")
            )
            .order_by(Company.corporate_name)
            .all()
        )