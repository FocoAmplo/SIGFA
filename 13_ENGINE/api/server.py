import os
from datetime import datetime
from pathlib import Path
from typing import Any

from fastapi import Depends, FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, Field

from config.settings import APP_NAME, KNOWLEDGE_DIR, ROOT_DIR, VERSION


CLIENT_INBOX_DIR = ROOT_DIR / "02_BANCO_DADOS" / "ENTRADAS_CLIENTES"
SIGFA_API_KEY = os.getenv("SIGFA_API_KEY", "sigfa-dev-key-change-me")
MAX_UPLOAD_BYTES = 25 * 1024 * 1024
ALLOWED_UPLOAD_EXTENSIONS = {
    ".csv",
    ".doc",
    ".docx",
    ".jpeg",
    ".jpg",
    ".pdf",
    ".png",
    ".txt",
    ".xls",
    ".xlsx",
}
api_key_header = APIKeyHeader(name="X-SIGFA-API-Key", auto_error=False)


def _safe_name(value: str) -> str:
    allowed = [char if char.isalnum() else "-" for char in value.strip().lower()]
    return "-".join("".join(allowed).split("-")) or "cliente"


def exigir_api_key(api_key: str | None = Depends(api_key_header)) -> None:
    if api_key != SIGFA_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key invalida ou ausente.",
        )


def _validar_extensao_arquivo(filename: str | None) -> str:
    suffix = Path(filename or "").suffix.lower()
    if suffix not in ALLOWED_UPLOAD_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Tipo de arquivo nao permitido. Extensoes aceitas: {sorted(ALLOWED_UPLOAD_EXTENSIONS)}",
        )
    return suffix


class PerguntaRequest(BaseModel):
    pergunta: str = Field(..., min_length=1, description="Pergunta enviada pelo agente ChatGPT ao SIGFA.")
    contexto: dict[str, Any] | None = Field(
        default=None,
        description="Contexto opcional enviado pelo agente, como empresa, area, processo ou periodo analisado.",
    )


class PerguntaResponse(BaseModel):
    pergunta: str
    resposta: str
    fonte: str


class AcessoClienteRequest(BaseModel):
    nome: str = Field(..., min_length=2)
    email: str = Field(..., min_length=5)
    empresa: str = Field(..., min_length=2)
    mensagem: str | None = None


class TextoClienteRequest(BaseModel):
    empresa: str = Field(..., min_length=2)
    contato: str = Field(..., min_length=2)
    titulo: str = Field(..., min_length=2)
    conteudo: str = Field(..., min_length=1)


app = FastAPI(
    title="SIGFA API",
    description="API para conectar o agente ChatGPT ao sistema SIGFA.",
    version=VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://focoamplo.com.br",
        "https://www.focoamplo.com.br",
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Sistema"], operation_id="verificarSaudeApi")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "app": APP_NAME,
        "version": VERSION,
    }


@app.get(
    "/auth/me",
    tags=["Autenticacao"],
    dependencies=[Depends(exigir_api_key)],
    operation_id="validarChaveAcessoSigfa",
)
def auth_me() -> dict[str, str]:
    return {
        "status": "autenticado",
        "app": APP_NAME,
        "auth": "api-key",
    }


@app.get("/sigfa/status", tags=["SIGFA"], operation_id="consultarStatusSigfa")
def sigfa_status() -> dict[str, Any]:
    return {
        "engine": "online",
        "knowledge_base_found": KNOWLEDGE_DIR.exists(),
        "knowledge_dir": str(KNOWLEDGE_DIR),
    }


@app.post("/sigfa/pergunta", response_model=PerguntaResponse, tags=["SIGFA"], operation_id="perguntarAoSigfa")
def perguntar(payload: PerguntaRequest) -> PerguntaResponse:
    return PerguntaResponse(
        pergunta=payload.pergunta,
        resposta=(
            "Conexao com a API do SIGFA realizada com sucesso. "
            "O proximo passo e conectar este endpoint ao leitor da base de conhecimento."
        ),
        fonte="SIGFA Engine API",
    )


@app.post("/sigfa/diagnostico", tags=["SIGFA"], operation_id="solicitarDiagnosticoSigfa")
def diagnostico(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "status": "recebido",
        "mensagem": "Solicitacao de diagnostico recebida pela API do SIGFA.",
        "entrada": payload,
    }


@app.post("/cliente/acesso/solicitar", tags=["Portal do Cliente"], operation_id="solicitarAcessoClienteSigfa")
def solicitar_acesso(payload: AcessoClienteRequest) -> dict[str, Any]:
    return {
        "status": "recebido",
        "mensagem": "Solicitacao de acesso recebida. A equipe Foco Amplo ira validar o cadastro.",
        "cliente": {
            "nome": payload.nome,
            "email": payload.email,
            "empresa": payload.empresa,
        },
    }


@app.post(
    "/cliente/envios/texto",
    tags=["Portal do Cliente"],
    dependencies=[Depends(exigir_api_key)],
    operation_id="enviarTextoClienteSigfa",
)
def receber_texto_cliente(payload: TextoClienteRequest) -> dict[str, Any]:
    cliente_dir = CLIENT_INBOX_DIR / _safe_name(payload.empresa)
    cliente_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    arquivo = cliente_dir / f"{timestamp}-texto.txt"
    arquivo.write_text(
        "\n".join(
            [
                f"Empresa: {payload.empresa}",
                f"Contato: {payload.contato}",
                f"Titulo: {payload.titulo}",
                "",
                payload.conteudo,
            ]
        ),
        encoding="utf-8",
    )

    return {
        "status": "recebido",
        "mensagem": "Texto recebido e registrado para processamento pelo SIGFA.",
        "arquivo": str(arquivo.relative_to(ROOT_DIR)),
    }


@app.post(
    "/cliente/envios/arquivo",
    tags=["Portal do Cliente"],
    dependencies=[Depends(exigir_api_key)],
    operation_id="enviarArquivoClienteSigfa",
)
def receber_arquivo_cliente(
    empresa: str = Form(...),
    contato: str = Form(...),
    descricao: str = Form(""),
    arquivo: UploadFile = File(...),
) -> dict[str, Any]:
    cliente_dir = CLIENT_INBOX_DIR / _safe_name(empresa)
    cliente_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    extensao = _validar_extensao_arquivo(arquivo.filename)
    destino = cliente_dir / f"{timestamp}-{_safe_name(Path(arquivo.filename or 'arquivo').stem)}{extensao}"

    with destino.open("wb") as output:
        arquivo.file.seek(0)
        copied = 0
        while chunk := arquivo.file.read(1024 * 1024):
            copied += len(chunk)
            if copied > MAX_UPLOAD_BYTES:
                destino.unlink(missing_ok=True)
                raise HTTPException(
                    status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                    detail="Arquivo excede o limite de 25 MB.",
                )
            output.write(chunk)

    metadados = destino.with_suffix(destino.suffix + ".meta.txt")
    metadados.write_text(
        "\n".join(
            [
                f"Empresa: {empresa}",
                f"Contato: {contato}",
                f"Descricao: {descricao}",
                f"Arquivo original: {arquivo.filename}",
                f"Content-Type: {arquivo.content_type}",
                f"Tamanho bytes: {destino.stat().st_size}",
            ]
        ),
        encoding="utf-8",
    )

    return {
        "status": "recebido",
        "mensagem": "Arquivo recebido e registrado para leitura pelo SIGFA.",
        "arquivo": str(destino.relative_to(ROOT_DIR)),
        "metadados": str(metadados.relative_to(ROOT_DIR)),
    }
