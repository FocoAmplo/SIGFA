import hashlib


class Encryption:

    @staticmethod
    def sha256(file_bytes: bytes):

        return hashlib.sha256(file_bytes).hexdigest()