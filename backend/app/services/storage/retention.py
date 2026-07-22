from datetime import datetime


class Retention:

    @staticmethod
    def new_version(version: int):

        return version + 1

    @staticmethod
    def archive_name(filename: str, version: int):

        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")

        return f"{filename}_v{version}_{timestamp}"