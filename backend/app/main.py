from fastapi import FastAPI

from backend.app.auth.routes import router as auth_router

app = FastAPI(title="SIGFA Platform API")
app.include_router(auth_router)


@app.get("/", summary="Plataforma SIGFA status")
def read_root():
    return {"sistema": "SIGFA", "versao": "1.0", "status": "online"}


@app.get("/health", summary="Health check")
def health_check():
    return {"status": "ok"}
