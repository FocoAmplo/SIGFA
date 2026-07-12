from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.method import MethodCreate
from ...schemas.method import MethodResponse
from ...schemas.method import MethodUpdate
from ...services.knowledge import MethodService

router = APIRouter(
    prefix="/knowledge/methods",
    tags=["Knowledge - Methods"],
)


@router.get("/", response_model=list[MethodResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return MethodService.get_all(db)


@router.get("/{id}", response_model=MethodResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    method = MethodService.get_by_id(db, id)

    if not method:
        raise HTTPException(status_code=404, detail="Método não encontrado.")

    return method


@router.post("/", response_model=MethodResponse)
def create(
    method: MethodCreate,
    db: Session = Depends(get_db),
):
    return MethodService.create(db, method)


@router.put("/{id}", response_model=MethodResponse)
def update(
    id: int,
    method: MethodUpdate,
    db: Session = Depends(get_db),
):
    db_method = MethodService.update(db, id, method)

    if not db_method:
        raise HTTPException(status_code=404, detail="Método não encontrado.")

    return db_method


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = MethodService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Método não encontrado.")

    return {"deleted": deleted}
