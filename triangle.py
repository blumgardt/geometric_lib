def area(a, h): 
    '''
    Returns the area of a triangle
        Parameters:
            a (int): side of the triangle, decimal number
            h (int): height of the triangle, decimal number
        Return value:
            area (int): decimal number, area of the triangle using the formula
    Example:
        print(area(r))

        Input: a = 4; h = 10
        Output: 20
    '''

    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Returns the perimeter of a triangle
        Parameters:
            a (int): first side of the triangle, decimal number
            b (int): second side of the triangle, decimal number
            c (int): third side of the triangle, decimal number
        Return value:
            perimeter (int): decimal number, perimeter of the triangle using the formula
    Example:
        print(perimeter(r))

        Input: a = 4; b = 3; c = 5
        Output: 12
    '''
    
    return a + b + c 
