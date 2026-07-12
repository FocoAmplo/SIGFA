from pathlib import Path

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    UploadFile,
    status,
)
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from ..auth.dependencies import get_current_user
from ..database.session import get_db
from ..models.company import Company
from ..models.document import Document
from ..schemas.company import CompanyResponse as CompanyRead
from ..schemas.document import DocumentRead

router = APIRouter(
    prefix="/empresas",
    tags=["Empresas"],
)

UPLOAD_DIR = Path("storage/empresas")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.get("/", response_model=list[CompanyRead])
def listar_empresas(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    empresas = db.query(Company).order_by(Company.nome).all()
    return empresas


@router.post(
    "/{company_id}/documentos",
    response_model=DocumentRead,
    status_code=status.HTTP_201_CREATED,
)
def upload_documento(
    company_id: int,
    titulo: str = Form(...),
    descricao: str = Form(""),
    arquivo: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    empresa = (
        db.query(Company)
        .filter(Company.id == company_id)
        .first()
    )

    if not empresa:
        raise HTTPException(
            status_code=404,
            detail="Empresa não encontrada.",
        )

    pasta_empresa = UPLOAD_DIR / f"EMP{company_id:07d}" / "documentos"
    pasta_empresa.mkdir(parents=True, exist_ok=True)

    destino = pasta_empresa / arquivo.filename

    with open(destino, "wb") as buffer:
        buffer.write(arquivo.file.read())

    documento = Document(
        titulo=titulo,
        descricao=descricao,
        filename=arquivo.filename,
        filepath=str(destino),
        empresa_id=company_id,
        uploaded_by=current_user.id,
    )

    db.add(documento)
    db.commit()
    db.refresh(documento)

    return documento


@router.get(
    "/{company_id}/documentos",
    response_model=list[DocumentRead],
)
def listar_documentos(
    company_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    documentos = (
        db.query(Document)
        .filter(Document.empresa_id == company_id)
        .all()
    )

    return documentos


@router.get(
    "/{company_id}/documentos/{document_id}/download"
)
def download_documento(
    company_id: int,
    document_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    documento = (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.empresa_id == company_id,
        )
        .first()
    )

    if not documento:
        raise HTTPException(
            status_code=404,
            detail="Documento não encontrado.",
        )

    caminho = Path(documento.filepath)

    if not caminho.exists():
        raise HTTPException(
            status_code=404,
            detail="Arquivo não encontrado.",
        )

    return FileResponse(
        path=str(caminho),
        filename=documento.filename,
        media_type="application/octet-stream",
    )


@router.delete(
    "/{company_id}/documentos/{document_id}"
)
def excluir_documento(
    company_id: int,
    document_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    documento = (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.empresa_id == company_id,
        )
        .first()
    )

    if not documento:
        raise HTTPException(
            status_code=404,
            detail="Documento não encontrado.",
        )

    caminho = Path(documento.filepath)

    if caminho.exists():
        caminho.unlink()

    db.delete(documento)
    db.commit()

    return {
        "message": "Documento removido com sucesso."
    }