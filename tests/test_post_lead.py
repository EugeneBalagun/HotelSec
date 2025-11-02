# tests/test_post_lead.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
import jwt
import random
from app.config import settings

client = TestClient(app)

# tests/test_post_lead.py
def test_create_lead_with_jwt():
    payload = {"sub": "testuser"}
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    headers = {"Authorization": f"Bearer {token}"}

    random_email = f"john{random.randint(1000,9999)}@example.com"
    payload_data = {
        "name": "John Doe",
        "email": random_email,
        "phone": "1234567890"
    }

    response = client.post("/lead", json=payload_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "lead_id" in data
    assert data["message"] == "Lead created successfully"
