from __future__ import annotations

from typing import Any


class MemoryEngine:
    """
    Responsável por consolidar a memória utilizada pelo
    Centro de Inteligência.

    Não acessa banco de dados.
    Não consulta IA.
    Apenas organiza a memória disponível.
    """

    def build(
        self,
        company: dict[str, Any] | None = None,
        memory: dict[str, Any] | None = None,
        conversation: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:

        company = company or {}
        memory = memory or {}

        return {

            "company_id": company.get("id"),

            "tenant_id": company.get("tenant_id"),

            "history": memory.get("history", []),

            "conversation": conversation or [],

            "entities": memory.get("entities", []),

            "previous_diagnosis": memory.get(
                "previous_diagnosis",
                []
            ),

        }


memory_engine = MemoryEngine()