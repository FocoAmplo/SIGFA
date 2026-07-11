from datetime import datetime, timedelta
from typing import Any, Dict, Optional

import jwt
from fastapi import HTTPException, status

SECRET_KEY = "SIGFA_2026_SUPER_SECRET_KEY_64_BYTES_CHANGE_THIS_NOW_123456789"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(
    subject: Dict[str, Any],
    expires_delta: Optional[timedelta] = None,
) -> str:

    if expires_delta is None:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    now = datetime.utcnow()

    payload = subject.copy()

    payload.update(
        {
            "iat": now,
            "exp": now + expires_delta,
        }
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_access_token(token: str) -> Dict[str, Any]:

    try:

        print("=" * 80)
        print("TOKEN RECEBIDO")
        print(token)

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        print("PAYLOAD")
        print(payload)

        if "sub" not in payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido",
            )

        return payload

    except jwt.ExpiredSignatureError:
        print("TOKEN EXPIRADO")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado",
        )

    except jwt.InvalidTokenError as e:
        print("ERRO JWT:")
        print(e)

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
        )
    