# app/main.py

import logging  # <-- Import the logging module
from fastapi import FastAPI, HTTPException
from .operations import add_op, subtract_op, multiply_op, divide_op

# --- Add this configuration block ---
logging.basicConfig(
    level=logging.INFO,  # Set the minimum level of messages to log
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', # Define the log message format
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file named app.log
        logging.StreamHandler()       # Also log to the console
    ]
)

# Get a logger instance for this file
logger = logging.getLogger(__name__)
# --- End of new block ---


app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Root endpoint was accessed.") # <-- Example of an info log
    return {"message": "FastAPI Calculator is running!"}

@app.get("/add")
def add(num1: float, num2: float):
    result = add_op(num1, num2)
    # Log the successful operation
    logger.info(f"Add operation: {num1} + {num2} = {result}")
    return {"result": result}

@app.get("/subtract")
def subtract(num1: float, num2: float):
    result = subtract_op(num1, num2)
    # Log the successful operation
    logger.info(f"Subtract operation: {num1} - {num2} = {result}")
    return {"result": result}

@app.get("/multiply")
def multiply(num1: float, num2: float):
    result = multiply_op(num1, num2)
    # Log the successful operation
    logger.info(f"Multiply operation: {num1} * {num2} = {result}")
    return {"result": result}

@app.get("/divide")
def divide(num1: float, num2: float):
    try:
        result = divide_op(num1, num2)
        # Log the successful operation
        logger.info(f"Divide operation: {num1} / {num2} = {result}")
        return {"result": result}
    except ValueError as e:
        # Log the error *before* raising the exception
        logger.warning(f"Division by zero attempt: {num1} / {num2}") # <-- Log a warning for handled errors
        raise HTTPException(status_code=400, detail=str(e))