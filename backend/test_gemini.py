from backend.ai.gemini_client import ask_gemini

resultado = ask_gemini(
    "Responda apenas: API funcionando."
)

print(resultado)