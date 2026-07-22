from __future__ import annotations


class SpecialistRepository:
    """
    Especialistas disponíveis.
    """

    def load(self) -> list:

        return [
            "CEO",
            "Financeiro",
            "Comercial",
            "RH",
            "Qualidade",
            "Produção",
            "Logística",
            "Jurídico",
            "Construção",
        ]


specialist_repository = SpecialistRepository()