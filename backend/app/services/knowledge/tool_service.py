from sqlalchemy.orm import Session

from backend.app.models.tool import Tool
from backend.app.schemas.tool import ToolCreate
from backend.app.schemas.tool import ToolUpdate


class ToolService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Tool)
            .order_by(Tool.name)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        tool_id: int,
    ):

        return (
            db.query(Tool)
            .filter(Tool.id == tool_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        tool: ToolCreate,
    ):

        db_tool = Tool(**tool.model_dump())

        db.add(db_tool)

        db.commit()

        db.refresh(db_tool)

        return db_tool

    @staticmethod
    def update(
        db: Session,
        tool_id: int,
        tool: ToolUpdate,
    ):

        db_tool = (
            db.query(Tool)
            .filter(Tool.id == tool_id)
            .first()
        )

        if not db_tool:
            return None

        update_data = tool.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_tool,
                key,
                value,
            )

        db.commit()

        db.refresh(db_tool)

        return db_tool

    @staticmethod
    def delete(
        db: Session,
        tool_id: int,
    ):

        db_tool = (
            db.query(Tool)
            .filter(Tool.id == tool_id)
            .first()
        )

        if not db_tool:
            return False

        db.delete(db_tool)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(Tool)
            .filter(
                Tool.name.ilike(f"%{text}%")
            )
            .order_by(Tool.name)
            .all()
        )

    @staticmethod
    def activate(
        db: Session,
        tool_id: int,
    ):

        db_tool = (
            db.query(Tool)
            .filter(Tool.id == tool_id)
            .first()
        )

        if not db_tool:
            return None

        db_tool.active = True

        db.commit()

        db.refresh(db_tool)

        return db_tool

    @staticmethod
    def deactivate(
        db: Session,
        tool_id: int,
    ):

        db_tool = (
            db.query(Tool)
            .filter(Tool.id == tool_id)
            .first()
        )

        if not db_tool:
            return None

        db_tool.active = False

        db.commit()

        db.refresh(db_tool)

        return db_tool
