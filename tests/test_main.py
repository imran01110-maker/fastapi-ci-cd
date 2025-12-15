from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_health():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_sum():
    res = client.get("/sum?a=2&b=3")
    assert res.json()["result"] == 5
