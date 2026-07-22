from datetime import datetime


class Metadata:

    @staticmethod
    def build(
        tenant_id: str,
        filename: str,
        category: str,
        uploaded_by: str,
    ):

        return {

            "tenant": tenant_id,

            "filename": filename,

            "category": category,

            "uploaded_by": uploaded_by,

            "created_at": datetime.utcnow().isoformat(),

            "status": "stored",

            "version": 1

        }