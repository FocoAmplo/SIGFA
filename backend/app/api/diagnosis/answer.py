from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.answer import AnswerCreate
from ...schemas.answer import AnswerResponse
from ...schemas.answer import AnswerUpdate
from ...services.diagnosis import AnswerService

router = APIRouter(
    prefix="/answer",
    tags=["Answer"],
)


@router.get("/", response_model=list[AnswerResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return AnswerService.get_all(db)


@router.get("/{id}", response_model=AnswerResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    answer = AnswerService.get_by_id(db, id)

    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found.")

    return answer


@router.post("/", response_model=AnswerResponse)
def create(
    answer: AnswerCreate,
    db: Session = Depends(get_db),
):
    return AnswerService.create(db, answer)


@router.put("/{id}", response_model=AnswerResponse)
def update(
    id: int,
    answer: AnswerUpdate,
    db: Session = Depends(get_db),
):
    db_answer = AnswerService.update(db, id, answer)

    if not db_answer:
        raise HTTPException(status_code=404, detail="Answer not found.")

    return db_answer


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = AnswerService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Answer not found.")

    return {"deleted": deleted}
