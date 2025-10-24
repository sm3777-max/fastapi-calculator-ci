# tests/test_integration.py

from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app

# Create a client to interact with your app
client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI Calculator is running!"}

def test_add_endpoint():
    response = client.get("/add?num1=5&num2=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_subtract_endpoint():
    response = client.get("/subtract?num1=10&num2=4")
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_multiply_endpoint():
    response = client.get("/multiply?num1=6&num2=2")
    assert response.status_code == 200
    assert response.json() == {"result": 12}

def test_divide_endpoint():
    response = client.get("/divide?num1=20&num2=5")
    assert response.status_code == 200
    assert response.json() == {"result": 4}

# This is the most important integration test.
# It checks if your app correctly handles the "divide by zero" error
# and returns the 400 status code we programmed in main.py.
def test_divide_by_zero_endpoint():
    response = client.get("/divide?num1=10&num2=0")
    # Check that the status code is 400 (Bad Request)
    assert response.status_code == 400
    # Check that the JSON response contains our error detail
    assert "detail" in response.json()
    assert response.json()["detail"] == "Cannot divide by zero"

def test_invalid_parameters():
    # Test what happens if you send text instead of numbers
    response = client.get("/add?num1=ten&num2=five")
    # FastAPI should automatically return a 422 error
    assert response.status_code == 422