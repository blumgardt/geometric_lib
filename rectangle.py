import unittest
'''Import the unittest for testing'''

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
        '''Tests the area function with one side as 0, expecting an area of 0.'''
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_square_mul(self):
        '''Tests the area function with equal length and width, forming a square. Expects area = side^2.'''
        res = area(10, 10)
        self.assertEqual(res, 100)
    
    def test_perimeter_add(self):
        '''Tests the perimeter function with typical length and width values to verify perimeter calculation.'''
        res = perimeter(2, 5)
        self.assertEqual(res, 14)
    
    def test_negative_area(self):
        '''Tests the area function with a negative length, expecting the result to be the product of length and width.'''
        res = area(-3, 5)
        self.assertEqual(res, -15)

    def test_large_perimeter(self):
        '''Tests the perimeter function with large values for length and width to verify correct handling of large inputs.'''
        res = perimeter(100000, 50000)
        self.assertEqual(res, 300000)