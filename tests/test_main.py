import langchain_app


def test_main_uses_gemini_key_fallback(monkeypatch, capsys):
    captured = {}

    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    monkeypatch.setenv("GEMINI_API_KEY", "test-gemini-key")
    monkeypatch.setattr(langchain_app, "load_dotenv", lambda: None)

    class DummyModel:
        def __init__(self, **kwargs):
            captured["kwargs"] = kwargs

        def stream(self, query):
            return iter([type("Chunk", (), {"content": "hello"})()])

    monkeypatch.setattr(langchain_app, "ChatGoogleGenerativeAI", DummyModel)

    langchain_app.main()

    captured_output = capsys.readouterr().out
    assert "Streaming response" in captured_output
    assert captured["kwargs"]["google_api_key"] == "test-gemini-key"
