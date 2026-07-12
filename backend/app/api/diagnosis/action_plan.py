from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.action_plan import ActionPlanCreate
from ...schemas.action_plan import ActionPlanResponse
from ...schemas.action_plan import ActionPlanUpdate
from ...services.diagnosis import ActionPlanService

router = APIRouter(
    prefix="/action-plan",
    tags=["Action Plan"],
)


@router.get("/", response_model=list[ActionPlanResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return ActionPlanService.get_all(db)


@router.get("/{id}", response_model=ActionPlanResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    action_plan = ActionPlanService.get_by_id(db, id)

    if not action_plan:
        raise HTTPException(status_code=404, detail="Action plan not found.")

    return action_plan


@router.post("/", response_model=ActionPlanResponse)
def create(
    action_plan: ActionPlanCreate,
    db: Session = Depends(get_db),
):
    return ActionPlanService.create(db, action_plan)


@router.put("/{id}", response_model=ActionPlanResponse)
def update(
    id: int,
    action_plan: ActionPlanUpdate,
    db: Session = Depends(get_db),
):
    db_action_plan = ActionPlanService.update(db, id, action_plan)

    if not db_action_plan:
        raise HTTPException(status_code=404, detail="Action plan not found.")

    return db_action_plan


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = ActionPlanService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Action plan not found.")

    return {"deleted": deleted}
