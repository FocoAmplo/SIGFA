from .provider import StorageProvider


class Downloader:

    def __init__(self, bucket_name: str):

        self.provider = StorageProvider(bucket_name)
        self.bucket = self.provider.get_bucket()

    def download(
        self,
        remote_path: str,
        local_path: str,
    ):

        blob = self.bucket.blob(remote_path)

        blob.download_to_filename(local_path)

        return local_path