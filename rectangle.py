def area(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise TypeError("Both length and width must be numbers")
    if a < 0 or b < 0:
        raise ValueError("Values cannot be negative")
    return a * b

def perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")
    return 2 * (length + width)

