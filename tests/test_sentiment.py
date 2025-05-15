from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_homepage():
    response = client.get("/")
    assert response.status_code == 200
    assert "Text Summarizer" in response.text

def test_summarize_short_text():
    response = client.post("/summarize", data={"text": "Too short to summarize."})
    assert response.status_code == 200
    assert "Text too short to summarize" in response.text

def test_summarize_valid_text():
    long_text = (
        "Machine learning is a method of data analysis" 
        "that automates analytical model building. "
        "It is a branch of artificial intelligence" 
        based on the idea that systems can learn from data, "
        "identify patterns and make decisions" 
        "with minimal human intervention."
    )
    response = client.post("/summarize", data={"text": long_text})
    assert response.status_code == 200
    assert "Summary" in response.text
