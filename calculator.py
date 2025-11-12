
import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b
def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ValueError("raise ZeroDivisionError")
    return b/a

def power(a, b):
    return math.pow(a, b)

def log(a, base=10):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log(a, base)

def exp(a, b):
    return b ** a
