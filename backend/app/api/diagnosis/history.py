from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.history import HistoryCreate
from ...schemas.history import HistoryResponse
from ...schemas.history import HistoryUpdate
from ...services.diagnosis import HistoryService

router = APIRouter(
    prefix="/history",
    tags=["History"],
)


@router.get("/", response_model=list[HistoryResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return HistoryService.get_all(db)


@router.get("/{id}", response_model=HistoryResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    history = HistoryService.get_by_id(db, id)

    if not history:
        raise HTTPException(status_code=404, detail="History not found.")

    return history


@router.post("/", response_model=HistoryResponse)
def create(
    history: HistoryCreate,
    db: Session = Depends(get_db),
):
    return HistoryService.create(db, history)


@router.put("/{id}", response_model=HistoryResponse)
def update(
    id: int,
    history: HistoryUpdate,
    db: Session = Depends(get_db),
):
    db_history = HistoryService.update(db, id, history)

    if not db_history:
        raise HTTPException(status_code=404, detail="History not found.")

    return db_history


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = HistoryService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="History not found.")

    return {"deleted": deleted}
