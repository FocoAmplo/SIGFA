from sqlalchemy.orm import Session

from backend.app.models.attachment import Attachment
from backend.app.schemas.attachment import AttachmentCreate
from backend.app.schemas.attachment import AttachmentUpdate


class AttachmentService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Attachment)
            .order_by(Attachment.id)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        attachment_id: int,
    ):

        return (
            db.query(Attachment)
            .filter(Attachment.id == attachment_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        attachment: AttachmentCreate,
    ):

        db_attachment = Attachment(**attachment.model_dump())

        db.add(db_attachment)

        db.commit()

        db.refresh(db_attachment)

        return db_attachment

    @staticmethod
    def update(
        db: Session,
        attachment_id: int,
        attachment: AttachmentUpdate,
    ):

        db_attachment = (
            db.query(Attachment)
            .filter(Attachment.id == attachment_id)
            .first()
        )

        if not db_attachment:
            return None

        update_data = attachment.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_attachment,
                key,
                value,
            )

        db.commit()

        db.refresh(db_attachment)

        return db_attachment

    @staticmethod
    def delete(
        db: Session,
        attachment_id: int,
    ):

        db_attachment = (
            db.query(Attachment)
            .filter(Attachment.id == attachment_id)
            .first()
        )

        if not db_attachment:
            return False

        db.delete(db_attachment)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Attachment)
            .filter(
                Attachment.file_name.ilike(f"%{text}%")
            )
            .order_by(Attachment.id)
            .all()
        )
