# FastAPI Calculator CI Project

This is a project for **Python for Web API Development** to demonstrate a CI/CD pipeline for a simple FastAPI calculator application.

It includes:
* A FastAPI application with basic arithmetic operations.
* Logging for all endpoints.
* Unit, Integration, and End-to-End (Playwright) tests.
* A GitHub Actions workflow to automate testing.

## How to Set Up and Run the Application

1.  **Clone the repository:**
    ```bash
    git clone <YOUR_REPO_URL_HERE>
    cd fastapi-calculator-ci
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

4.  **Run the application:**
    ```bash
    uvicorn app.main:app --reload
    ```

The application will be running at `http://127.0.0.1:8000`.

## How to Run Tests

1.  **Run unit and integration tests:**
    ```bash
    pytest tests/test_unit.py tests/test_integration.py
    ```

2.  **Run end-to-end tests:**
    (Make sure the application is running in another terminal first!)
    ```bash
    pytest tests/test_e2e.py --base-url [http://127.0.0.1:8000](http://127.0.0.1:8000)
    ```