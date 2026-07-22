from .provider import StorageProvider


class Vault:

    def __init__(self, bucket_name: str):
        self.provider = StorageProvider(bucket_name)
        self.bucket = self.provider.get_bucket()

    def create_tenant(self, tenant_id: str):

        folders = [
            "documents/",
            "knowledge/",
            "intelligence/",
            "reports/",
            "logs/",
            "backups/",
            "temp/"
        ]

        for folder in folders:

            blob = self.bucket.blob(
                f"{tenant_id}/{folder}.keep"
            )

            if not blob.exists():

                blob.upload_from_string("")