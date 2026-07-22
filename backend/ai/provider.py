from backend.ai.providers.gemini_provider import gemini_provider


class AIProvider:
    """
    Camada única de acesso aos modelos de IA.

    Atualmente:
        - Gemini

    Futuramente:
        - Vertex AI
        - OpenAI
        - Claude
        - Mistral
        - Local LLM
    """

    def chat(self, payload: dict, documents: list[str]) -> dict:
        return gemini_provider.chat(
            payload=payload,
            documents=documents,
        )


provider = AIProvider()