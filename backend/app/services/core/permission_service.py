from sqlalchemy.orm import Session

from app.models.permission import Permission
from app.schemas.permission import PermissionCreate
from app.schemas.permission import PermissionUpdate


class PermissionService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Permission)
            .order_by(Permission.name)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        permission_id: int,
    ):

        return (
            db.query(Permission)
            .filter(Permission.id == permission_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        permission: PermissionCreate,
    ):

        db_permission = Permission(**permission.model_dump())

        db.add(db_permission)

        db.commit()

        db.refresh(db_permission)

        return db_permission

    @staticmethod
    def update(
        db: Session,
        permission_id: int,
        permission: PermissionUpdate,
    ):

        db_permission = (
            db.query(Permission)
            .filter(Permission.id == permission_id)
            .first()
        )

        if not db_permission:
            return None

        update_data = permission.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_permission,
                key,
                value,
            )

        db.commit()

        db.refresh(db_permission)

        return db_permission

    @staticmethod
    def delete(
        db: Session,
        permission_id: int,
    ):

        db_permission = (
            db.query(Permission)
            .filter(Permission.id == permission_id)
            .first()
        )

        if not db_permission:
            return False

        db.delete(db_permission)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Permission)
            .filter(
                Permission.name.ilike(f"%{text}%")
            )
            .order_by(Permission.name)
            .all()
        )