from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.tool import ToolCreate
from ...schemas.tool import ToolResponse
from ...schemas.tool import ToolUpdate
from ...services.knowledge import ToolService

router = APIRouter(
    prefix="/knowledge/tools",
    tags=["Knowledge - Tools"],
)


@router.get("/", response_model=list[ToolResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return ToolService.get_all(db)


@router.get("/{id}", response_model=ToolResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    tool = ToolService.get_by_id(db, id)

    if not tool:
        raise HTTPException(status_code=404, detail="Ferramenta não encontrada.")

    return tool


@router.post("/", response_model=ToolResponse)
def create(
    tool: ToolCreate,
    db: Session = Depends(get_db),
):
    return ToolService.create(db, tool)


@router.put("/{id}", response_model=ToolResponse)
def update(
    id: int,
    tool: ToolUpdate,
    db: Session = Depends(get_db),
):
    db_tool = ToolService.update(db, id, tool)

    if not db_tool:
        raise HTTPException(status_code=404, detail="Ferramenta não encontrada.")

    return db_tool


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = ToolService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Ferramenta não encontrada.")

    return {"deleted": deleted}
