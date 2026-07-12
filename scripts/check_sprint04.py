from pathlib import Path

files = [
    "backend/app/services/diagnosis/diagnosis_service.py",
    "backend/app/services/diagnosis/answer_service.py",
    "backend/app/services/diagnosis/score_service.py",
    "backend/app/services/diagnosis/action_plan_service.py",
    "backend/app/services/diagnosis/attachment_service.py",
    "backend/app/services/diagnosis/history_service.py",
    "backend/app/services/diagnosis/ai_recommendation_service.py",
    "backend/app/api/diagnosis/diagnosis.py",
    "backend/app/api/diagnosis/answer.py",
    "backend/app/api/diagnosis/score.py",
    "backend/app/api/diagnosis/action_plan.py",
    "backend/app/api/diagnosis/attachment.py",
    "backend/app/api/diagnosis/history.py",
    "backend/app/api/diagnosis/ai_recommendation.py",
]

print("=" * 60)
print("SPRINT 04 VALIDATION")
print("=" * 60)

missing = []

for file in files:
    path = Path(file)

    if path.exists():
        print(f"[ OK ] {file}")
    else:
        print(f"[FAIL] {file}")
        missing.append(file)

print("=" * 60)

if not missing:
    print("Sprint 04 completa.")
else:
    print("Arquivos pendentes:")
    for item in missing:
        print(item)