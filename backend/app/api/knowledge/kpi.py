from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.kpi import KPICreate
from ...schemas.kpi import KPIResponse
from ...schemas.kpi import KPIUpdate
from ...services.knowledge import KPIService

router = APIRouter(
    prefix="/knowledge/kpis",
    tags=["Knowledge - KPIs"],
)


@router.get("/", response_model=list[KPIResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return KPIService.get_all(db)


@router.get("/{id}", response_model=KPIResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    kpi = KPIService.get_by_id(db, id)

    if not kpi:
        raise HTTPException(status_code=404, detail="KPI não encontrado.")

    return kpi


@router.post("/", response_model=KPIResponse)
def create(
    kpi: KPICreate,
    db: Session = Depends(get_db),
):
    return KPIService.create(db, kpi)


@router.put("/{id}", response_model=KPIResponse)
def update(
    id: int,
    kpi: KPIUpdate,
    db: Session = Depends(get_db),
):
    db_kpi = KPIService.update(db, id, kpi)

    if not db_kpi:
        raise HTTPException(status_code=404, detail="KPI não encontrado.")

    return db_kpi


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = KPIService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="KPI não encontrado.")

    return {"deleted": deleted}
