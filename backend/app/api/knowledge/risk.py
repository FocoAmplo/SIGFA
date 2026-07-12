from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.risk import RiskCreate
from ...schemas.risk import RiskResponse
from ...schemas.risk import RiskUpdate
from ...services.knowledge import RiskService

router = APIRouter(
    prefix="/knowledge/risks",
    tags=["Knowledge - Risks"],
)


@router.get("/", response_model=list[RiskResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return RiskService.get_all(db)


@router.get("/{id}", response_model=RiskResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    risk = RiskService.get_by_id(db, id)

    if not risk:
        raise HTTPException(status_code=404, detail="Risco não encontrado.")

    return risk


@router.post("/", response_model=RiskResponse)
def create(
    risk: RiskCreate,
    db: Session = Depends(get_db),
):
    return RiskService.create(db, risk)


@router.put("/{id}", response_model=RiskResponse)
def update(
    id: int,
    risk: RiskUpdate,
    db: Session = Depends(get_db),
):
    db_risk = RiskService.update(db, id, risk)

    if not db_risk:
        raise HTTPException(status_code=404, detail="Risco não encontrado.")

    return db_risk


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = RiskService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Risco não encontrado.")

    return {"deleted": deleted}
