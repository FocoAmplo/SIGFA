import tempfile
import unittest
from pathlib import Path

from backend.app.services.document_analysis import extract_text_from_file


class DocumentAnalysisTests(unittest.TestCase):
    def test_extract_text_from_text_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "contexto.txt"
            path.write_text("Receita cresceu 10% e o risco de liquidez aumentou", encoding="utf-8")
            extracted = extract_text_from_file(path)
            self.assertIn("Receita", extracted)
            self.assertIn("liquidez", extracted)

    def test_extract_text_from_csv_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "dados.csv"
            path.write_text("mes,receita\njan,100\nfev,120\n", encoding="utf-8")
            extracted = extract_text_from_file(path)
            self.assertIn("mes", extracted)
            self.assertIn("receita", extracted)


if __name__ == "__main__":
    unittest.main()
