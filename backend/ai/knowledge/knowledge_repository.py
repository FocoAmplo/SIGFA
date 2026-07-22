from __future__ import annotations

from typing import Any

from backend.ai.knowledge.company_repository import company_repository
from backend.ai.knowledge.construction_repository import construction_repository
from backend.ai.knowledge.document_repository import document_repository
from backend.ai.knowledge.history_repository import history_repository
from backend.ai.knowledge.indicator_repository import indicator_repository
from backend.ai.knowledge.specialist_repository import specialist_repository


class KnowledgeRepository:
    """
    Centraliza todas as fontes de conhecimento do SIGFA.

    Esta camada NÃO consulta a IA.
    Apenas organiza e entrega conhecimento estruturado
    para o AI Orchestrator.
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

        return {

            "company": company_repository.load(company),

            "documents": document_repository.load(documents),

            "history": history_repository.load(company),

            "indicators": indicator_repository.load(company),

            "construction": construction_repository.load(company),

            "specialists": specialist_repository.load(company),

            "assessment": assessment,

        }


knowledge_repository = KnowledgeRepository()