from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_ai_chat_mock_provider():
    response = client.post(
        "/ai/chat",
        json={
            "provider": "mock",
            "messages": [{"role": "user", "content": "Explique o conceito de gestão por processos."}],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["provider"] == "mock"
    assert "response" in body
    assert body["response"]
