import math
'''Import the math module that provides math constants and formulas'''

def area(r):
    '''
    Returns the area of a circle
        Parameter:
            r (int): radius, decimal number
        Return value:
            area (int): decimal number, area of the circle using the formula
    '''

    return math.pi * r * r


def perimeter(r):
    '''
    Returns the perimeter of a circle
        Parameter:
            r (int): radius, decimal number
        Return value:
            perimeter (int): decimal number, perimeter of the circle using the formula
    '''

    return 2 * math.pi * r

print(perimeter(5))
