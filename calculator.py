
import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
<<<<<<< HEAD
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a
def log(a, b):
    if b < 0:
        raise ValueError
    else:
        return math.log(b, a)

def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def power(a, b):
    return math.pow(a, b)

def log(a, base=10):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log(a, base)

def exp(a, b):
    return b ** a
