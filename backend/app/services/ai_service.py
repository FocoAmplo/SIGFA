from __future__ import annotations

import json
from time import perf_counter
from typing import Any

from fastapi import UploadFile
from sqlalchemy.orm import Session

from backend.ai.orchestrator import ai_orchestrator
from backend.app.models.action_plan import ActionPlan
from backend.app.models.ai_log import AILog
from backend.app.models.ai_recommendation import AIRecommendation
from backend.app.models.attachment import Attachment
from backend.app.models.diagnosis import Diagnosis
from backend.app.models.history import History
from backend.app.models.notification import Notification
from backend.app.models.score import Score
from backend.app.services.document_service import DocumentService


class AIService:
    """Ponto único do fluxo corporativo de Inteligência do SIGFA."""

    def __init__(self):
        self.documents = DocumentService()

    async def chat(self, prompt: str, files: list[UploadFile], db: Session, user: Any) -> dict[str, Any]:
        started_at = perf_counter()
        tenant_id = f"company_{user.company_id:07d}"
        company = {"id": user.company_id, "tenant_id": tenant_id}
        try:
            documents = [
                await self.documents.upload(file, db, user.company_id, user.id, tenant_id)
                for file in files
            ]
            raw = ai_orchestrator.chat(
                prompt=prompt,
                documents=documents,
                company=company,
                user={"id": user.id, "name": user.name, "email": user.email},
                memory={},
            )
            result = self._official_response(raw, documents, company, user, started_at)
            diagnosis_id = self._persist(db, result, prompt, documents, user)
            db.commit()
            result["metadata"]["diagnosis_id"] = diagnosis_id
            return result
        except Exception:
            db.rollback()
            raise

    @staticmethod
    def _official_response(raw: dict[str, Any], documents: list[dict[str, Any]], company: dict[str, Any], user: Any, started_at: float) -> dict[str, Any]:
        conversation = raw.get("conversation", [])
        if not isinstance(conversation, list):
            conversation = [{"role": "assistant", "content": str(conversation)}]
        return {
            "conversation": conversation,
            "diagnosis": raw.get("diagnosis") or {},
            "recommendations": raw.get("recommendations") or [],
            "action_plan": raw.get("action_plan") or [],
            "alerts": raw.get("alerts") or [],
            "indicators": raw.get("indicators") or [],
            "dashboard_updates": raw.get("dashboard_updates") or raw.get("dashboard") or {},
            "metadata": {
                "tenant_id": company["tenant_id"],
                "company_id": company["id"],
                "user_id": user.id,
                "documents": [{key: item[key] for key in ("id", "name", "bucket", "path", "hash", "status")} for item in documents],
                **(raw.get("metadata") or {}),
            },
            "confidence": raw.get("confidence", 0),
            "processing_time": round((perf_counter() - started_at) * 1000, 2),
        }

    @staticmethod
    def _persist(db: Session, result: dict[str, Any], prompt: str, documents: list[dict[str, Any]], user: Any) -> int:
        data = result["diagnosis"]
        diagnosis = Diagnosis(
            company_id=user.company_id,
            title=data.get("title") or "Diagnóstico do Centro de Inteligência",
            status="COMPLETED",
            score=data.get("score"),
            maturity_level=data.get("maturity_level"),
            risk_level=data.get("risk_level"),
        )
        db.add(diagnosis)
        db.flush()
        for document in documents:
            db.add(Attachment(diagnosis_id=diagnosis.id, file_name=document["name"], file_path=document["path"], file_type=document["metadata"].get("content_type")))
        for recommendation in result["recommendations"]:
            text = recommendation.get("recommendation", recommendation) if isinstance(recommendation, dict) else str(recommendation)
            db.add(AIRecommendation(diagnosis_id=diagnosis.id, agent_code="SIGFA", recommendation=text, confidence=result["confidence"], accepted=False))
        for index, action in enumerate(result["action_plan"]):
            data = action if isinstance(action, dict) else {"description": str(action)}
            db.add(ActionPlan(diagnosis_id=diagnosis.id, recommendation_code=f"AI-{index + 1}", action_description=data.get("description") or data.get("action"), responsible=data.get("responsible"), priority=data.get("priority")))
        for indicator in result["indicators"]:
            if isinstance(indicator, dict) and indicator.get("value") is not None:
                db.add(Score(diagnosis_id=diagnosis.id, indicator_code=indicator.get("code") or indicator.get("name"), value=indicator["value"]))
        db.add(History(diagnosis_id=diagnosis.id, event_type="AI_ANALYSIS", description=prompt, user_name=user.name))
        for alert in result["alerts"]:
            text = alert.get("message", alert) if isinstance(alert, dict) else str(alert)
            db.add(Notification(company_id=user.company_id, title="Alerta SIGFA", message=text, notification_type="AI"))
        db.add(AILog(agent_code="SIGFA", diagnosis_id=diagnosis.id, prompt=prompt, response=json.dumps(result, ensure_ascii=False), execution_time_ms=result["processing_time"]))
        return diagnosis.id


ai_service = AIService()
