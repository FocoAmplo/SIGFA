from pathlib import Path

from .provider import StorageProvider
from .vault import Vault


class Uploader:

    def __init__(self, bucket_name: str):

        self.provider = StorageProvider(bucket_name)
        self.bucket = self.provider.get_bucket()
        self.vault = Vault(bucket_name)

    def upload_file(
        self,
        tenant_id: str,
        local_file: str,
        destination: str,
        filename: str | None = None,
    ):

        self.vault.create_tenant(tenant_id)

        file_name = filename or Path(local_file).name

        blob = self.bucket.blob(
            f"{tenant_id}/{destination}/{file_name}"
        )

        blob.upload_from_filename(local_file)

        return blob.name
