from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..auth.dependencies import get_current_user
from ..database.session import get_db
from ..models.company import Company
from ..models.document import Document
from ..models.user import User

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/overview")
def dashboard_overview(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    empresas = db.query(Company).count()
    usuarios = db.query(User).count()
    documentos = db.query(Document).count()

    if current_user.empresa_id:
        empresas_filtradas = db.query(Company).filter(Company.id == current_user.empresa_id).count()
    else:
        empresas_filtradas = empresas

    empresa_nome = None
    if current_user.empresa_id is not None:
        empresa = db.query(Company).filter(Company.id == current_user.empresa_id).first()
        empresa_nome = empresa.nome if empresa else None

    return {
        "empresa_id": current_user.empresa_id,
        "empresa_nome": empresa_nome,
        "total_empresas": empresas,
        "total_usuarios": usuarios,
        "total_documentos": documentos,
        "empresas_visiveis": empresas_filtradas,
    }
