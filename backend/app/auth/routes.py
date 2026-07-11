from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from ..auth.auth_service import AuthService
from ..auth.dependencies import get_current_user, require_permission
from ..auth.external_auth import ExternalAuthService
from ..database.session import get_db
from ..schemas.external_login import ExternalLoginRequest
from ..schemas.login import LoginRequest
from ..schemas.refresh import RefreshResponse, RefreshTokenRequest
from ..schemas.token import Token
from ..schemas.user import UserRead

router = APIRouter(tags=["auth"])

auth_service = AuthService()
external_auth_service = ExternalAuthService()


@router.post("/login", response_model=Token)
def login(
    credentials: LoginRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    return auth_service.authenticate_user(db, credentials.email, credentials.senha, request)


@router.post("/external")
def external_login(
    payload: ExternalLoginRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    return external_auth_service.authenticate(db, payload.email, payload.name, payload.provider, request)


@router.post("/refresh", response_model=RefreshResponse)
def refresh_token(
    payload: RefreshTokenRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    return auth_service.refresh_access_token(db, payload.refresh_token, request)


@router.post("/logout")
def logout(
    payload: RefreshTokenRequest,
    current_user: UserRead = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    auth_service.logout_user(db, payload.refresh_token)
    return JSONResponse({"detail": "Logout realizado com sucesso"})


@router.get("/me", response_model=UserRead)
def read_me(current_user: UserRead = Depends(get_current_user)):
    return current_user


@router.get("/status")
def auth_status():
    return {"auth": "online"}


@router.get("/permissions")
def permissions(current_user: UserRead = Depends(require_permission("auth:read"))):
    return {"permissions": current_user.permissions}
