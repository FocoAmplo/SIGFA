from __future__ import annotations

import json
import os
from typing import Any

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiProvider:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY não encontrada."
            )

        self.model = os.getenv(
            "MODEL_NAME",
            "gemini-2.5-pro"
        )

        self.client = genai.Client(
            api_key=api_key
        )

    def _default_response(
        self,
        text: str = ""
    ) -> dict[str, Any]:

        return {

            "conversation": [

                {
                    "role": "assistant",
                    "content": text
                }

            ] if text else [],

            "company": {},

            "documents": [],

            "knowledge": {},

            "diagnosis": {

                "summary": text

            } if text else {},

            "dashboard": {

                "health": 0,
                "finance": 0,
                "commercial": 0,
                "production": 0,
                "quality": 0,
                "hr": 0

            },

            "indicators": [],

            "charts": [],

            "alerts": [],

            "recommendations": [],

            "action_plan": [],

            "timeline": [],

            "logs": [],

            "specialist": {},

            "construction": {

                "projects": [],
                "budgets": [],
                "measurements": [],
                "suppliers": [],
                "teams": []

            }

        }

    def chat(
        self,
        payload: dict,
        documents: list[str],
    ) -> dict:

        response = self.client.models.generate_content(

            model=self.model,

            contents=json.dumps(
                payload,
                ensure_ascii=False,
            )

        )

        text = (response.text or "").strip()

        if text.startswith("```json"):

            text = (
                text
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

        try:

            result = json.loads(text)

        except Exception:

            result = self._default_response(text)

        default = self._default_response()

        for key, value in default.items():

            result.setdefault(key, value)

        result["documents"] = documents

        return result


gemini_provider = GeminiProvider()