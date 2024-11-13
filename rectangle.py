import unittest

def area(a, b): 
    '''
    Returns the area of a rectangle
        Parameters:
            a (int): length, decimal number
            b (int): width, decimal number
        Return value:
            area (int): decimal number, area of the rectangle using the formula
    Example:
        print(area(r))

        Input: a = 2; b = 3
        Output: 6
    '''

    return a * b 

def perimeter(a, b): 
    '''
    Returns the perimeter of a rectangle
        Parameters:
            a (int): length, decimal number
            b (int): width, decimal number
        Return value:
            perimeter (int): decimal number, perimeter of the rectangle using the formula
    Example:
        print(perimeter(r))

        Input: a = 2; b = 3
        Output: 12
    '''

    return (a + b) * 2

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    
    def test_perimeter_add(self):
        res = perimeter(2, 5)
        self.assertEqual(res, 14)
    
    def test_negative_area(self):
        res = area(-3, 5)
        self.assertEqual(res, -15)

    def test_large_perimeter(self):
        res = perimeter(100000, 50000)
        self.assertEqual(res, 300000)