from backend.app.services.storage.provider import StorageProvider

provider = StorageProvider("sigfa-vault-dev")

print(provider.bucket_exists())