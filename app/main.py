import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel  # <-- Import BaseModel

from .operations import add_op, subtract_op, multiply_op, divide_op

# Logging configuration (keep as-is)
logger = logging.getLogger(__name__)

app = FastAPI()

# --- Templates Section (Correct) ---
templates = Jinja2Templates(directory="app/templates")

# --- Pydantic Model (NEW) ---
# This defines the structure of the JSON data your frontend will send
# e.g., {"a": 10.0, "b": 20.0}
class Numbers(BaseModel):
    a: float
    b: float

# --- Root Endpoint (Correct) ---
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """Serves the main HTML calculator page."""
    return templates.TemplateResponse("index.html", {"request": request})

# --- API Endpoints (NEW - This is the fix) ---

@app.post("/add")
def add_numbers(nums: Numbers):
    """Adds two numbers."""
    try:
        result = add_op(nums.a, nums.b)
        return {"result": result}
    except Exception as e:
        logger.error(f"Error in add operation: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/subtract")
def subtract_numbers(nums: Numbers):
    """Subtracts two numbers."""
    try:
        result = subtract_op(nums.a, nums.b)
        return {"result": result}
    except Exception as e:
        logger.error(f"Error in subtract operation: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/multiply")
def multiply_numbers(nums: Numbers):
    """Multiplies two numbers."""
    try:
        result = multiply_op(nums.a, nums.b)
        return {"result": result}
    except Exception as e:
        logger.error(f"Error in multiply operation: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/divide")
def divide_numbers(nums: Numbers):
    """
    Divides two numbers.
    Returns a specific error message for division by zero.
    """
    if nums.b == 0:
        # This JSON response matches your test expectation and frontend code
        logger.warning("Division by zero attempted.")
        return {"error": "Cannot divide by zero"}
    
    try:
        result = divide_op(nums.a, nums.b)
        return {"result": result}
    except Exception as e:
        logger.error(f"Error in divide operation: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")