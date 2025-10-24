from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app

# Create a client to interact with your app
client = TestClient(app)

def test_root_endpoint():
    """
    Test the root (/) endpoint.
    It should return 200 OK and an HTML page.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers['content-type'] == 'text/html; charset=utf-8'
    assert "FastAPI Calculator" in response.text

def test_add_endpoint():
    """Test the /add endpoint using POST with a JSON body."""
    response = client.post("/add", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_subtract_endpoint():
    """Test the /subtract endpoint using POST with a JSON body."""
    response = client.post("/subtract", json={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_multiply_endpoint():
    """Test the /multiply endpoint using POST with a JSON body."""
    response = client.post("/multiply", json={"a": 6, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 12}

def test_divide_endpoint():
    """Test the /divide endpoint using POST with a JSON body."""
    response = client.post("/divide", json={"a": 20, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 4}

def test_divide_by_zero_endpoint():
    """
    Test the /divide endpoint for division by zero.
    It should return a 400 Bad Request status.
    """
    response = client.post("/divide", json={"a": 10, "b": 0})
    
    # Check that the status code is 400 (Bad Request)
    assert response.status_code == 400
    
    # Check that the JSON response contains our error detail
    assert "detail" in response.json()
    assert response.json()["detail"] == "Cannot divide by zero"

def test_invalid_parameters():
    """
    Test sending invalid data (strings instead of numbers).
    Pydantic should catch this and return a 422 Unprocessable Entity.
    """
    response = client.post("/add", json={"a": "ten", "b": "five"})
    
    # Check that the status code is 422
    assert response.status_code == 422