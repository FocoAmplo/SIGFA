from dotenv import load_dotenv
from google.cloud import storage
import os

load_dotenv()


class StorageProvider:

    def __init__(self, bucket_name: str):

        project = os.getenv("GOOGLE_CLOUD_PROJECT")

        self.client = storage.Client(
            project=project
        )

        self.bucket = self.client.bucket(bucket_name)

    def get_bucket(self):
        return self.bucket

    def bucket_exists(self):
        return self.bucket.exists()

    def list_objects(self, prefix=""):
        return self.client.list_blobs(
            self.bucket,
            prefix=prefix
        )