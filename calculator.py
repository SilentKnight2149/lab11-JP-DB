
import math

def square_root(x):
    try:
        return math.sqrt(x)
    except ValueError:
        raise ValueError("Cannot compute square root of negative number") if a<0
    
def hypoetnuse(a, b):
    return math.hypot(a, b)



# First example

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

def log(a, b=10):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log(a, b)

def exp(a, b):
    return b ** a

