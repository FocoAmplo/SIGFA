from __future__ import annotations

from typing import Any

from backend.ai.assessment import assessment_engine
from backend.ai.engines.context_engine import context_engine
from backend.ai.engines.intelligence_engine import intelligence_engine
from backend.ai.engines.knowledge_engine import knowledge_engine
from backend.ai.engines.memory_engine import memory_engine
from backend.ai.engines.rules_engine import rules_engine
from backend.ai.provider import provider


class AIOrchestrator:
    """
    Coordenador central da Inteligência do SIGFA.

    Fluxo Oficial:

    Assessment Engine
            │
            ▼
    Knowledge Engine
            │
            ▼
    Context Engine
            │
            ▼
    Memory Engine
            │
            ▼
    Rules Engine
            │
            ▼
    Intelligence Engine
            │
            ▼
    AI Provider
    """

    def chat(
        self,
        prompt: str,
        documents: list[dict[str, Any]],
        company: dict[str, Any],
        user: dict[str, Any],
        memory: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        memory = memory or {}

        assessment = assessment_engine.execute(
            company=company,
            documents=documents,
            information={
                "prompt": prompt,
                "user": user,
            },
        )

        knowledge = knowledge_engine.build(
            company=company,
            documents=documents,
            assessment=assessment,
        )

        memory_context = memory_engine.build(
            company=company,
            memory=memory,
            conversation=[],
        )

        context = context_engine.build(
            company=company,
            user=user,
            documents=documents,
            assessment=assessment,
            knowledge=knowledge,
            memory=memory_context,
        )

        rules = rules_engine.build(
            company=company,
            assessment=assessment,
        )

        payload = intelligence_engine.execute(
            prompt=prompt,
            context=context,
            knowledge=knowledge,
            rules=rules,
            memory=memory_context,
        )

        return provider.chat(
            payload=payload,
            documents=documents,
        )


ai_orchestrator = AIOrchestrator()