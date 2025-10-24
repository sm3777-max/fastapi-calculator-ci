from fastapi import FastAPI, HTTPException
# The '.' tells Python to import from the current directory (the 'app' folder)
from .operations import add_op, subtract_op, multiply_op, divide_op

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI Calculator is running!"}

@app.get("/add")
def add(num1: float, num2: float):
    return {"result": add_op(num1, num2)}

@app.get("/subtract")
def subtract(num1: float, num2: float):
    return {"result": subtract_op(num1, num2)}

@app.get("/multiply")
def multiply(num1: float, num2: float):
    return {"result": multiply_op(num1, num2)}

@app.get("/divide")
def divide(num1: float, num2: float):
    try:
        return {"result": divide_op(num1, num2)}
    except ValueError as e:
        # This returns a user-friendly 400 error
        raise HTTPException(status_code=400, detail=str(e))