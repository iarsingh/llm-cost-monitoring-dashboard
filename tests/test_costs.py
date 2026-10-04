from fastapi.testclient import TestClient
from llmcost.main import app

client = TestClient(app)


def test_totals_and_budget():
    payload = client.post("/costs", json={"lines": [{'service': 'small', 'cost': 4}, {'service': 'large', 'cost': 9}], "budget": 12.0}).json()
    assert payload["total"] == 13.0
    assert payload["over_budget"] is True
    assert payload["applied"] is False
