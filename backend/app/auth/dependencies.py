from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from ..database.session import get_db
from ..models.user import User
from ..schemas.user import UserResponse
from .jwt_handler import decode_access_token

security = HTTPBearer()


def get_current_user(
    request: Request,
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> UserResponse:

    payload = getattr(request.state, "user_payload", None)

    if payload is None:
        payload = decode_access_token(credentials.credentials)

    user_id = int(payload["sub"])

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if user is None or not user.active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário inválido",
        )

    return UserResponse(
        id=user.id,
        uuid=user.uuid,
        company_id=user.company_id,
        profile_id=user.profile_id,
        name=user.name,
        email=user.email,
        phone=user.phone,
        avatar=user.avatar,
        active=user.active,
        last_login=user.last_login,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )


def require_permission(permission: str):
    def dependency(
        current_user: UserResponse = Depends(get_current_user),
    ) -> UserResponse:

        if permission not in getattr(current_user, "permissions", []):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permissão insuficiente",
            )

        return current_user

    return dependency