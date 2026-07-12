import importlib

modules = [
    "app.services.diagnosis",
    "app.api.diagnosis",
]

print("=" * 60)
print("SIGFA DIAGNOSIS VALIDATION")
print("=" * 60)

for module in modules:
    try:
        importlib.import_module(module)
        print(f"[ OK ] {module}")
    except Exception as e:
        print(f"[FAIL] {module}")
        print(e)