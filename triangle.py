import unittest
'''Import the unittest for testing'''

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
        """Tests area of a triangle with height 0, expecting area = 0."""
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_square_mul(self):
        """Tests area of a triangle with base 10 and height 6, expecting area = 30."""
        res = area(10, 6)
        self.assertEqual(res, 30)
    
    def test_perimeter_add(self):
        """Tests perimeter of a triangle with sides 3, 5, and 4, expecting perimeter = 12."""
        res = perimeter(3, 5, 4)
        self.assertEqual(res, 12)
    
    def test_negative_area(self):
        """Tests area calculation with a negative base, expecting a negative area result if negative inputs are allowed."""
        res = area(-5, 10)
        self.assertEqual(res, -25)

    def test_large_perimeter(self):
        """Tests perimeter calculation with very large side values, ensuring no overflow errors."""
        res = perimeter(1000, 2000, 3000)
        self.assertEqual(res, 6000)