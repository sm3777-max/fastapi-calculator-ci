# tests/test_unit.py

import pytest
from app.operations import add_op, subtract_op, multiply_op, divide_op

# Test for the add operation
def test_add():
    assert add_op(10, 5) == 15
    assert add_op(-1, 1) == 0
    assert add_op(-1, -1) == -2

# Test for the subtract operation
def test_subtract():
    assert subtract_op(10, 5) == 5
    assert subtract_op(-1, 1) == -2
    assert subtract_op(5, 10) == -5

# Test for the multiply operation
def test_multiply():
    assert multiply_op(3, 5) == 15
    assert multiply_op(-1, 5) == -5
    assert multiply_op(0, 5) == 0

# Test for the divide operation
def test_divide():
    assert divide_op(10, 2) == 5
    assert divide_op(5, 2) == 2.5
    assert divide_op(-10, 2) == -5

# This is an important "edge case" test.
# We test that our code correctly raises a ValueError
# when we try to divide by zero, just as we programmed it to.
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide_op(10, 0)