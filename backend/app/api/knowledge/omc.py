from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.omc import OMCCreate
from ...schemas.omc import OMCResponse
from ...schemas.omc import OMCUpdate
from ...services.knowledge import OMCService

router = APIRouter(
    prefix="/knowledge/omc",
    tags=["Knowledge - OMC"],
)


@router.get("/", response_model=list[OMCResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return OMCService.get_all(db)


@router.get("/{id}", response_model=OMCResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    omc = OMCService.get_by_id(db, id)

    if not omc:
        raise HTTPException(status_code=404, detail="OMC não encontrado.")

    return omc


@router.post("/", response_model=OMCResponse)
def create(
    omc: OMCCreate,
    db: Session = Depends(get_db),
):
    return OMCService.create(db, omc)


@router.put("/{id}", response_model=OMCResponse)
def update(
    id: int,
    omc: OMCUpdate,
    db: Session = Depends(get_db),
):
    db_omc = OMCService.update(db, id, omc)

    if not db_omc:
        raise HTTPException(status_code=404, detail="OMC não encontrado.")

    return db_omc


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = OMCService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="OMC não encontrado.")

    return {"deleted": deleted}
