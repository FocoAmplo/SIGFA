from __future__ import annotations

from typing import Any


class IntelligenceEngine:
    """
    Consolida todas as informações antes da IA.

    Não chama o AI Provider.

    Apenas monta o payload oficial do SIGFA.
    """

    def execute(
        self,
        prompt: str,
        context: dict[str, Any],
        knowledge: dict[str, Any],
        rules: dict[str, Any],
        memory: dict[str, Any],
    ) -> dict[str, Any]:

        return {

            "prompt": prompt,

            "context": context,

            "knowledge": knowledge,

            "rules": rules,

            "memory": memory,

            "response_format": {

                "conversation": True,

                "diagnosis": True,

                "recommendations": True,

                "action_plan": True,

                "alerts": True,

                "indicators": True,

                "dashboard": True,

            }

        }


intelligence_engine = IntelligenceEngine()