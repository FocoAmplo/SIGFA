from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...database.session import get_db
from ...schemas.question import QuestionCreate
from ...schemas.question import QuestionResponse
from ...schemas.question import QuestionUpdate
from ...services.knowledge import QuestionService

router = APIRouter(
    prefix="/knowledge/questions",
    tags=["Knowledge - Questions"],
)


@router.get("/", response_model=list[QuestionResponse])
def get_all(
    db: Session = Depends(get_db),
):
    return QuestionService.get_all(db)


@router.get("/{id}", response_model=QuestionResponse)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    question = QuestionService.get_by_id(db, id)

    if not question:
        raise HTTPException(status_code=404, detail="Pergunta não encontrada.")

    return question


@router.post("/", response_model=QuestionResponse)
def create(
    question: QuestionCreate,
    db: Session = Depends(get_db),
):
    return QuestionService.create(db, question)


@router.put("/{id}", response_model=QuestionResponse)
def update(
    id: int,
    question: QuestionUpdate,
    db: Session = Depends(get_db),
):
    db_question = QuestionService.update(db, id, question)

    if not db_question:
        raise HTTPException(status_code=404, detail="Pergunta não encontrada.")

    return db_question


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = QuestionService.delete(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Pergunta não encontrada.")

    return {"deleted": deleted}
