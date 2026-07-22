from __future__ import annotations


class ConstructionRepository:
    """
    Base de conhecimento da Construção Civil.
    """

    def load(self) -> dict:

        return {

            "segment": "construction",

            "disciplines": [

                "Planejamento",

                "Orçamento",

                "Cronograma",

                "Qualidade",

                "Produção",

                "Segurança",

                "Custos",

                "BDI",

                "SINAPI",

                "BIM",

            ]

        }


construction_repository = ConstructionRepository()