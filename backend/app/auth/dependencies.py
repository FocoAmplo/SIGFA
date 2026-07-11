from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from ..database.session import get_db
from ..models.user import User
from ..schemas.user import UserRead
from .jwt_handler import decode_access_token

security = HTTPBearer()


def get_current_user(
    request: Request,
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> UserRead:

    payload = getattr(request.state, "user_payload", None)

    if payload is None:
        payload = decode_access_token(credentials.credentials)

    user_id = int(payload["sub"])

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if user is None or not user.ativo:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário inválido",
        )

    permissions = []

    if user.role:
        permissions = [
            permission.chave
            for permission in user.role.permissions
        ]

    return UserRead(
        id=user.id,
        nome=user.nome,
        email=user.email,
        role=user.role.nome if user.role else "",
        permissions=permissions,
        empresa_id=user.empresa_id,
        ativo=user.ativo,
        ultimo_login=user.ultimo_login,
        created_at=user.created_at,
    )


def require_permission(permission: str):
    def dependency(
        current_user: UserRead = Depends(get_current_user),
    ) -> UserRead:

        if permission not in current_user.permissions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permissão insuficiente",
            )

        return current_user

    return dependency