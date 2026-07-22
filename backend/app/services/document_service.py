from pathlib import Path
import hashlib
import tempfile
from typing import Any

from fastapi import UploadFile
from sqlalchemy.orm import Session

from backend.app.models.document import Document
from backend.app.services.document_analysis import extract_text_from_file
from backend.app.services.storage.classifier import Classifier
from backend.app.services.storage.metadata import Metadata
from backend.app.services.storage.uploader import Uploader


class DocumentService:
    """Fluxo oficial: Vault para arquivo e PostgreSQL para metadados."""

    BUCKET = "sigfa-vault-dev"

    def __init__(self):
        self._uploader: Uploader | None = None

    @property
    def uploader(self) -> Uploader:
        """Cria o cliente de armazenamento apenas no momento do upload."""
        if self._uploader is None:
            self._uploader = Uploader(self.BUCKET)
        return self._uploader

    async def upload(
        self,
        file: UploadFile,
        db: Session,
        company_id: int,
        user_id: int,
        tenant_id: str,
    ) -> dict[str, Any]:
        filename = Path(file.filename or "documento").name
        content = await file.read()
        content_hash = hashlib.sha256(content).hexdigest()
        category = Classifier.classify(filename)
        temp_path: str | None = None

        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=Path(filename).suffix) as temp:
                temp.write(content)
                temp_path = temp.name

            cloud_path = self.uploader.upload_file(
                tenant_id=tenant_id,
                local_file=temp_path,
                destination=category,
                filename=filename,
            )
            metadata = Metadata.build(
                tenant_id=tenant_id,
                filename=filename,
                category=category,
                uploaded_by=str(user_id),
            )
            metadata.update({
                "content_hash": content_hash,
                "content_type": file.content_type or "application/octet-stream",
                "size_bytes": len(content),
                "bucket": self.BUCKET,
                "path": cloud_path,
            })
            document = Document(
                tenant_id=tenant_id,
                company_id=company_id,
                uploaded_by=user_id,
                title=filename,
                filename=filename,
                content_type=file.content_type,
                content_hash=content_hash,
                storage_bucket=self.BUCKET,
                storage_path=cloud_path,
                status="STORED",
                metadata_=metadata,
            )
            db.add(document)
            db.flush()
            return {
                "id": document.id,
                "name": filename,
                "bucket": self.BUCKET,
                "path": cloud_path,
                "hash": content_hash,
                "status": document.status,
                "metadata": metadata,
                "content": extract_text_from_file(temp_path),
            }
        finally:
            if temp_path:
                Path(temp_path).unlink(missing_ok=True)
