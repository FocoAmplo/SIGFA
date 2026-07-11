from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from .jwt_handler import decode_access_token


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, exempt_paths=None):
        super().__init__(app)
        self.exempt_paths = exempt_paths or [
            "/",
            "/health",
            "/openapi.json",
            "/docs",
            "/redoc",
            "/auth/login",
            "/auth/refresh",
        ]

    async def dispatch(self, request: Request, call_next) -> Response:
        request.state.user_payload = None
        if any(request.url.path.startswith(path) for path in self.exempt_paths):
            return await call_next(request)

        authorization = request.headers.get("Authorization")
        if authorization and authorization.startswith("Bearer "):
            token = authorization[7:]
            try:
                request.state.user_payload = decode_access_token(token)
            except Exception:
                request.state.user_payload = None

        return await call_next(request)
