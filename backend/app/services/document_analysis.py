from pathlib import Path
import csv
import json


def extract_text_from_file(path: str | Path) -> str:
    file_path = Path(path)
    if not file_path.exists():
        return ""

    extension = file_path.suffix.lower()

    if extension in {".txt", ".md", ".json", ".csv"}:
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        if extension == ".json":
            try:
                payload = json.loads(text)
                return json.dumps(payload, ensure_ascii=False, indent=2)
            except json.JSONDecodeError:
                return text
        if extension == ".csv":
            rows = []
            with file_path.open("r", encoding="utf-8", errors="ignore", newline="") as handle:
                for row in csv.reader(handle):
                    rows.append(" | ".join(row))
            return "\n".join(rows)
        return text

    if extension in {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".xml"}:
        return f"Conteúdo potencialmente extraível de {file_path.name} via integração futura com parser empresarial."

    return f"Arquivo anexado: {file_path.name}"
