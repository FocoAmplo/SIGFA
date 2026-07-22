from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from backend.app.database.session import get_db

from .schemas import PublicLeadCreate
from .schemas import PublicLeadResponse
from .schemas import PublicStatusResponse
from .service import public_lead_service


router = APIRouter(
    prefix="/public",
    tags=["GPT Público"],
)


@router.get(
    "/status",
    response_model=PublicStatusResponse,
)
def public_status():

    return {
        "status": "online",
        "service": "SIGFA GPT Público",
        "version": "1.0",
    }


@router.post(
    "/lead",
    response_model=PublicLeadResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_public_lead(
    payload: PublicLeadCreate,
    db: Session = Depends(get_db),
):

    return public_lead_service.create_lead(
        db=db,
        data=payload,
    )