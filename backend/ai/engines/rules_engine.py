from __future__ import annotations

from typing import Any


class RulesEngine:
    """
    Responsável pelas regras corporativas do SIGFA.
    """

    def build(
        self,
        company: dict[str, Any] | None = None,
        assessment: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        company = company or {}
        assessment = assessment or {}

        return {

            "tenant_id": company.get("tenant_id"),

            "company_id": company.get("id"),

            "assessment_authorized": assessment.get(
                "authorized",
                False
            ),

            "never_invent_data": True,

            "always_use_context": True,

            "respect_company_rules": True,

            "require_evidence": True,

            "generate_action_plan": True,

            "block_without_minimum_data": True,

        }


rules_engine = RulesEngine()