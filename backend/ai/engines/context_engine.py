from __future__ import annotations

from typing import Any


class ContextEngine:
    """
    Responsável por montar o contexto da empresa.
    """

    def build(
        self,
        company: dict[str, Any] | None = None,
        user: dict[str, Any] | None = None,
        documents: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:

        if company is None:
            company = {}

        return {
            "company": company,
            "user": user or {},
            "documents": documents or [],
            "segment": company.get("segment"),
            "size": company.get("size"),
            "location": company.get("location"),
            "profile": company.get("profile"),
        }


context_engine = ContextEngine()
