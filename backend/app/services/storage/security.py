from pathlib import PurePosixPath


class StorageSecurity:

    @staticmethod
    def build_path(
        tenant_id: str,
        category: str,
        filename: str,
    ):

        return str(
            PurePosixPath(
                tenant_id,
                category,
                filename,
            )
        )

    @staticmethod
    def validate_tenant(
        tenant_request: str,
        tenant_file: str,
    ):

        return tenant_request == tenant_file