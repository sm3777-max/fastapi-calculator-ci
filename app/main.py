import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# Import your math functions
from .operations import add_op, subtract_op, multiply_op, divide_op

# --- Logging Configuration ---
# (This assumes your logging is already configured as before)
# If not, add your logging.basicConfig here.
logger = logging.getLogger(__name__)

app = FastAPI()

# --- Templates Section ---
templates = Jinja2Templates(directory="app/templates")

# --- Pydantic Model ---
# This defines the JSON structure: {"a": 10.0, "b": 20.0}
class Numbers(BaseModel):
    a: float
    b: float

# --- Root Endpoint (FIXED) ---
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """Serves the main HTML calculator page."""
    # This is the corrected order to fix the DeprecationWarning
    return templates.TemplateResponse(request, "index.html")

# --- API Endpoints (FIXED) ---

@app.post("/add")
def add_numbers(nums: Numbers):
    """Adds two numbers from a JSON body."""
    try:
        result = add_op(nums.a, nums.b)
        logger.info(f"Add operation: {nums.a} + {nums.b} = {result}")
        return {"result": result}
    except Exception as e:
        logger.error(f"Error in add operation: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/subtract")
def subtract_numbers(nums: Numbers):
    """Subtracts two numbers from a JSON body."""
    try:
        result = subtract_op(nums.a, nums.b)
        logger.info(f"Subtract operation: {nums.a} - {nums.b} = {result}")
        return {"result": result}
    except Exception as e:
        logger.error(f"Error in subtract operation: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/multiply")
def multiply_numbers(nums: Numbers):
    """Multiplies two numbers from a JSON body."""
    try:
        result = multiply_op(nums.a, nums.b)
        logger.info(f"Multiply operation: {nums.a} * {nums.b} = {result}")
        return {"result": result}
    except Exception as e:
        logger.error(f"Error in multiply operation: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/divide")
def divide_numbers(nums: Numbers):
    """
    Divides two numbers from a JSON body.
    Handles division by zero by raising a 400 error.
    """
    try:
        result = divide_op(nums.a, nums.b)
        logger.info(f"Divide operation: {nums.a} / {nums.b} = {result}")
        return {"result": result}
    except ValueError as e:
        # This catches the "Cannot divide by zero" from operations.py
        logger.warning(f"Division by zero attempt: {nums.a} / {nums.b}")
        # This raises a 400 error, which your tests expect
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error in divide operation: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")