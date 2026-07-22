from __future__ import annotations

from typing import Any

from .checklist_engine import ChecklistEngine
from .company_profile import CompanyProfile
from .maturity_engine import MaturityEngine


class AssessmentEngine:
    """
    Primeiro estágio do Centro de Inteligência.

    Responsabilidades:

    - Identificar o perfil da empresa.
    - Avaliar documentos e informações.
    - Calcular maturidade.
    - Verificar nível mínimo.
    - Verificar nível completo.
    - Liberar ou bloquear o diagnóstico.
    """

    def __init__(self):

        self.checklist = ChecklistEngine()

        self.maturity = MaturityEngine()

    def execute(
        self,
        company: dict[str, Any],
        documents: list[dict[str, Any]],
        information: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        information = information or {}

        profile = CompanyProfile(
            company_id=company["id"],
            segment=company.get("segment", "construction"),
            subtype=company.get("subtype", "builder"),
            name=company.get("name"),
            regime=company.get("regime"),
            size=company.get("size"),
            state=company.get("state"),
        )

        checklist = self.checklist.evaluate(
            profile=profile,
            documents=documents,
            information=information,
        )

        maturity = self.maturity.calculate(checklist)

        minimum_completed = (
            checklist["minimum_level"] >= 100
        )

        complete_completed = (
            checklist["complete_level"] >= 100
        )

        return {

            "profile": profile,

            "checklist": checklist,

            "maturity": maturity,

            "minimum_completed": minimum_completed,

            "complete_completed": complete_completed,

            "authorized": minimum_completed

        }