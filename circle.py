import math
'''Import the math module that provides math constants and formulas'''

def area(r):
    if not isinstance(r, (int, float)):
        raise TypeError("Radius must be a number")
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * r * r

def perimeter(r):
    if not isinstance(r, (int, float)):
        raise TypeError("Radius must be a number")
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * r