from pathlib import Path


class Classifier:

    CATEGORIES = {

        ".pdf": "documents",

        ".doc": "documents",

        ".docx": "documents",

        ".xls": "documents",

        ".xlsx": "documents",

        ".csv": "documents",

        ".png": "documents",

        ".jpg": "documents",

        ".jpeg": "documents",

        ".dwg": "documents",

        ".ifc": "documents",

    }

    @classmethod
    def classify(cls, filename: str):

        extension = Path(filename).suffix.lower()

        return cls.CATEGORIES.get(
            extension,
            "documents"
        )