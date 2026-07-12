from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.ai import router as ai_router
from .api.auth import router as auth_router
from .api.company import router as company_router
from .api.dashboard import router as dashboard_router
from .api.diagnosis import action_plan_router
from .api.diagnosis import ai_recommendation_router
from .api.diagnosis import answer_router
from .api.diagnosis import attachment_router
from .api.diagnosis import diagnosis_router
from .api.diagnosis import history_router
from .api.diagnosis import score_router
from .api.knowledge import concept_router
from .api.knowledge import evidence_router
from .api.knowledge import kpi_router
from .api.knowledge import method_router
from .api.knowledge import omc_router
from .api.knowledge import question_router
from .api.knowledge import recommendation_router
from .api.knowledge import relationship_router
from .api.knowledge import risk_router
from .api.knowledge import tool_router
from .database.seed import create_database, seed_initial_data

app = FastAPI(
    title="SIGFA API",
    version="1.0.0",
    description="SIGFA backend API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@app.on_event("startup")
def startup_event():
    create_database()
    seed_initial_data()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(company_router)
app.include_router(ai_router)
app.include_router(dashboard_router)
app.include_router(diagnosis_router)
app.include_router(answer_router)
app.include_router(score_router)
app.include_router(action_plan_router)
app.include_router(attachment_router)
app.include_router(history_router)
app.include_router(ai_recommendation_router)
app.include_router(omc_router)
app.include_router(concept_router)
app.include_router(method_router)
app.include_router(tool_router)
app.include_router(kpi_router)
app.include_router(question_router)
app.include_router(evidence_router)
app.include_router(risk_router)
app.include_router(recommendation_router)
app.include_router(relationship_router)


@app.get("/", summary="Plataforma SIGFA status")
def read_root():
    return {"status": "online", "sistema": "SIGFA", "versao": "1.0.0"}


@app.get("/health", summary="Health check")
def health_check():
    return {"status": "ok"}
