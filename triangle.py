def area(a, h):
    if not all(isinstance(i, (int, float)) for i in [a, h]):
        raise TypeError("Base and height must be numbers")
    if a < 0 or h < 0:
        raise ValueError("Values cannot be negative")
    return a * h / 2

def perimeter(a, b, c):
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        raise TypeError("Sides must be numbers")
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise Exception("Invalid triangle sides")
    return a + b + c
