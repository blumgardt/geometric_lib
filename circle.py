import math
'''Import the math module that provides math constants and formulas'''

def area(r):
    '''
    Returns the area of a circle
        Parameter:
            r (int): radius, decimal number
        Return value:
            area (int): decimal number, area of the circle using the formula
    Example:
        print(area(r))

        Input: r = 4
        Output: 50.26548245743669
    '''

    return math.pi * r * r


def perimeter(r):
    '''
    Returns the perimeter of a circle
        Parameter:
            r (int): radius, decimal number
        Return value:
            perimeter (int): decimal number, perimeter of the circle using the formula
    Example:
        print(perimeter(r))

        Input: r = 5
        Output: 31.41592653589793
    '''

    return 2 * math.pi * r