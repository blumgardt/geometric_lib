import unittest

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

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_square_mul(self):
        res = area(10, 6)
        self.assertEqual(res, 30)
    
    def test_perimeter_add(self):
        res = perimeter(3, 5, 4)
        self.assertEqual(res, 12)
    
    def test_negative_area(self):
        res = area(-5, 10)
        self.assertEqual(res, -25)

    def test_large_perimeter(self):
        res = perimeter(1000, 2000, 3000)
        self.assertEqual(res, 6000)