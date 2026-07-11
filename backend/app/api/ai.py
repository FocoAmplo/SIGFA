from pathlib import Path
import shutil
import uuid
from typing import List, Literal

from fastapi import APIRouter, File, Form, Request, UploadFile
from pydantic import BaseModel

from ..services.document_analysis import extract_text_from_file

router = APIRouter(prefix="/ai", tags=["ai"])

UPLOAD_DIR = Path(__file__).resolve().parents[2] / "storage" / "ai_uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class Message(BaseModel):
    role: Literal["system", "user", "assistant"] = "user"
    content: str


class AnalysisItem(BaseModel):
    title: str
    description: str
    severity: Literal["Baixo", "Médio", "Alto", "Crítico"] = "Médio"


class ChatResponse(BaseModel):
    provider: str
    response: str
    analysis: dict
    files: List[str] = []
    status: str = "simulado"


def build_analysis(prompt: str, attachments: List[str], provider: str) -> dict:
    prompt_lower = (prompt or "").lower()

    diagnostics: List[AnalysisItem] = []
    indicators: List[dict] = []
    risks: List[AnalysisItem] = []
    recommendations: List[str] = []
    action_plan: List[str] = []

    if "financeiro" in prompt_lower or "receita" in prompt_lower or "custo" in prompt_lower:
        diagnostics.append(AnalysisItem(
            title="Performance financeira",
            description="Há sinais de necessidade de revisão do fluxo financeiro e de margem operacional.",
            severity="Alto",
        ))
        indicators.append({"name": "Margem líquida", "value": "+8%", "trend": "estável"})
        risks.append(AnalysisItem(
            title="Risco de liquidez",
            description="Aumento do tempo médio de recebimento pode impactar a capacidade de investimento.",
            severity="Médio",
        ))
    elif "qualidade" in prompt_lower or "processo" in prompt_lower:
        diagnostics.append(AnalysisItem(
            title="Qualidade operacional",
            description="Há oportunidade de padronizar processos e reduzir retrabalho.",
            severity="Médio",
        ))
        indicators.append({"name": "Taxa de retrabalho", "value": "12%", "trend": "em queda"})
    else:
        diagnostics.append(AnalysisItem(
            title="Contexto estratégico",
            description="O tema apresentado merece revisão das prioridades, riscos e próximos passos de execução.",
            severity="Médio",
        ))
        indicators.append({"name": "Nível de atenção", "value": "Elevado", "trend": "crescente"})

    if attachments:
        diagnostics.append(AnalysisItem(
            title="Documentos recebidos",
            description=f"{len(attachments)} anexos foram incorporados ao contexto do diagnóstico para análise posterior.",
            severity="Baixo",
        ))

    if "risco" in prompt_lower or "amea" in prompt_lower:
        risks.append(AnalysisItem(
            title="Risco de execução",
            description="A dependência de múltiplos stakeholders pode comprometer a velocidade de decisão.",
            severity="Alto",
        ))

    recommendations.extend([
        "Priorizar decisões com impacto direto em margem, risco e eficiência operacional.",
        "Estruturar um plano de ação com responsáveis, prazos e indicadores de acompanhamento.",
    ])

    action_plan.extend([
        "1. Consolidar o contexto do problema e definir critérios de decisão.",
        "2. Mapear riscos críticos e definir ações corretivas em até 15 dias.",
        "3. Acompanhar indicadores semanais e revisar o plano de execução mensalmente.",
    ])

    summary = (
        f"Diagnóstico gerado via {provider} com foco em contexto estratégico, riscos e execução."
    )

    return {
        "summary": summary,
        "diagnostics": [item.dict() for item in diagnostics],
        "indicators": indicators,
        "risks": [item.dict() for item in risks],
        "recommendations": recommendations,
        "action_plan": action_plan,
    }


async def save_upload(upload: UploadFile) -> str:
    if not upload.filename:
        return ""

    extension = Path(upload.filename).suffix.lower()
    if extension and extension not in {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".csv", ".xml", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".mp3", ".wav", ".mp4", ".mov", ".txt"}:
        return upload.filename

    filename = f"{uuid.uuid4().hex}{extension}"
    destination = UPLOAD_DIR / filename
    with destination.open("wb") as buffer:
        shutil.copyfileobj(upload.file, buffer)
    return upload.filename


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: Request,
    provider: str = Form(default="mock"),
    prompt: str = Form(default=""),
    files: List[UploadFile] = File(default_factory=list),
):
    content_type = request.headers.get("content-type", "")
    payload = {}

    if "application/json" in content_type:
        payload = await request.json()
        provider = payload.get("provider", provider)
        messages = payload.get("messages", [])
        prompt = next((message.get("content", "") for message in reversed(messages) if isinstance(message, dict) and message.get("role") == "user"), prompt)
        files = payload.get("files", [])

    attached_files: List[str] = []
    extracted_context: List[str] = []
    for item in files:
        if isinstance(item, UploadFile):
            saved_name = await save_upload(item)
            if saved_name:
                attached_files.append(saved_name)
                destination = UPLOAD_DIR / f"{uuid.uuid4().hex}{Path(item.filename).suffix.lower()}"
                with destination.open("wb") as buffer:
                    shutil.copyfileobj(item.file, buffer)
                extracted_context.append(extract_text_from_file(destination))
        elif isinstance(item, str):
            attached_files.append(item)

    if extracted_context:
        prompt = f"{prompt}\n\nContexto extraído dos anexos:\n" + "\n".join(extracted_context[:3])

    analysis = build_analysis(prompt, attached_files, provider)
    response_text = (
        f"Análise executiva pronta para {provider}. "
        f"O contexto recebido aponta para uma revisão estratégica com foco em risco, eficiência e plano de ação."
    )

    return ChatResponse(
        provider=provider,
        response=response_text,
        analysis=analysis,
        files=attached_files,
        status="simulado",
    )
