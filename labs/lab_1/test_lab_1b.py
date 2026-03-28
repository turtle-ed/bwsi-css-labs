import pytest
from lab_1b import simple_calculator


# --- Addition ---
def test_add_positive():
    assert simple_calculator("add", 3, 4) == 7

def test_add_negative():
    assert simple_calculator("add", -3, -4) == -7

def test_add_floats():
    assert simple_calculator("add", 1.5, 2.5) == 4.0


# --- Subtraction ---
def test_subtract_positive():
    assert simple_calculator("subtract", 10, 3) == 7

def test_subtract_negative_result():
    assert simple_calculator("subtract", 3, 10) == -7


# --- Multiplication ---
def test_multiply_positive():
    assert simple_calculator("multiply", 3, 4) == 12

def test_multiply_by_zero():
    assert simple_calculator("multiply", 5, 0) == 0

def test_multiply_negatives():
    assert simple_calculator("multiply", -3, -4) == 12


# --- Division ---
def test_divide_positive():
    assert simple_calculator("divide", 10, 2) == 5.0

def test_divide_returns_float():
    assert simple_calculator("divide", 7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        simple_calculator("divide", 5, 0)


# --- Invalid operation ---
def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation"):
        simple_calculator("mod", 5, 3)
