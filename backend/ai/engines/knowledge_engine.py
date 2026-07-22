from __future__ import annotations

from typing import Any

from backend.ai.knowledge.knowledge_repository import (
    knowledge_repository,
)


class KnowledgeEngine:
    """
    Knowledge Engine do SIGFA.

    Responsabilidades:
    - Consultar a Base Cognitiva.
    - Consolidar o conhecimento corporativo.
    - Entregar conhecimento estruturado ao AI Orchestrator.

    Não executa IA.
    Não consulta o AI Provider.
    Não produz diagnósticos.
    """

    def build(
        self,
        company: dict[str, Any] | None = None,
        documents: list[dict[str, Any]] | None = None,
        assessment: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        company = company or {}
        documents = documents or []
        assessment = assessment or {}

        return knowledge_repository.build(
            company=company,
            documents=documents,
            assessment=assessment,
        )


knowledge_engine = KnowledgeEngine()