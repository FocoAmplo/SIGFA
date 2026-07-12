import sys
from pathlib import Path
import importlib

# Descobre a raiz do projeto
ROOT = Path(__file__).resolve().parents[1]

# Adiciona backend ao PYTHONPATH
BACKEND = ROOT / "backend"
sys.path.insert(0, str(BACKEND))

modules = [
    "app.models",
    "app.schemas",
    "app.services",
    "app.api",
    "app.main",
]

print("=" * 60)
print("SIGFA BACKEND VALIDATION")
print("=" * 60)

errors = 0

for module in modules:
    try:
        importlib.import_module(module)
        print(f"[ OK ] {module}")
    except Exception as e:
        errors += 1
        print(f"[FAIL] {module}")
        print(f"       {e}")

print("=" * 60)

if errors == 0:
    print("VALIDAÇÃO CONCLUÍDA COM SUCESSO")
else:
    print(f"{errors} módulo(s) com erro")