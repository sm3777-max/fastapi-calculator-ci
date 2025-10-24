def add_op(num1: float, num2: float):
    return num1 + num2

def subtract_op(num1: float, num2: float):
    return num1 - num2

def multiply_op(num1: float, num2: float):
    return num1 * num2

def divide_op(num1: float, num2: float):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2