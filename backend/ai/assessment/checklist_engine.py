from typing import Any


class ChecklistEngine:

    """
    Responsável pelo Checklist Inteligente.
    Não realiza diagnóstico.
    """

    def evaluate(
        self,
        profile,
        documents: list[dict[str, Any]],
        information: dict[str, Any],
    ) -> dict:

        return {

            "segment": profile.segment,

            "subtype": profile.subtype,

            "minimum_level": 0,

            "complete_level": 0,

            "missing_documents": [],

            "missing_information": [],

            "status": "PENDING"

        }