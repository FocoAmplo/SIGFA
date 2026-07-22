from datetime import datetime


class Audit:

    @staticmethod
    def register(
        tenant_id: str,
        user: str,
        action: str,
        filename: str,
    ):

        return {

            "tenant": tenant_id,

            "user": user,

            "action": action,

            "filename": filename,

            "timestamp": datetime.utcnow().isoformat(),

        }