from sqlalchemy.orm import Session

from app.models.action_plan import ActionPlan
from app.schemas.action_plan import ActionPlanCreate
from app.schemas.action_plan import ActionPlanUpdate


class ActionPlanService:

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(ActionPlan)
            .order_by(ActionPlan.id)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        action_plan_id: int,
    ):

        return (
            db.query(ActionPlan)
            .filter(ActionPlan.id == action_plan_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        action_plan: ActionPlanCreate,
    ):

        db_action_plan = ActionPlan(**action_plan.model_dump())

        db.add(db_action_plan)

        db.commit()

        db.refresh(db_action_plan)

        return db_action_plan

    @staticmethod
    def update(
        db: Session,
        action_plan_id: int,
        action_plan: ActionPlanUpdate,
    ):

        db_action_plan = (
            db.query(ActionPlan)
            .filter(ActionPlan.id == action_plan_id)
            .first()
        )

        if not db_action_plan:
            return None

        update_data = action_plan.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_action_plan,
                key,
                value,
            )

        db.commit()

        db.refresh(db_action_plan)

        return db_action_plan

    @staticmethod
    def delete(
        db: Session,
        action_plan_id: int,
    ):

        db_action_plan = (
            db.query(ActionPlan)
            .filter(ActionPlan.id == action_plan_id)
            .first()
        )

        if not db_action_plan:
            return False

        db.delete(db_action_plan)

        db.commit()

        return True

    @staticmethod
    def search(
        db: Session,
        text: str,
    ):

        return (
            db.query(ActionPlan)
            .filter(
                ActionPlan.action_description.ilike(f"%{text}%")
            )
            .order_by(ActionPlan.id)
            .all()
        )
