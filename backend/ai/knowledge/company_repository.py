from __future__ import annotations


class CompanyRepository:
    """
    Recupera informações da empresa.
    """

    def load(
        self,
        company: dict | None,
    ) -> dict:

        return company or {}


company_repository = CompanyRepository()