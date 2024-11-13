import unittest
'''Import the unittest for testing'''

def area(a):
    '''
    Returns the area of a square
        Parameter:
            a (int): side of the square, decimal number
        Return value:
            area (int): decimal number, area of the square using the formula
    Example:
        print(area(r))

        Input: a = 4
        Output: 16
    '''

    return a * a


def perimeter(a):
    '''
    Returns the perimeter of a square
        Parameter:
            a (int): side of the square, decimal number
        Return value:
            perimeter (int): decimal number, perimeter of the square using the formula
    
    Example:
        print(perimeter(r))

        Input: a = 5
        Output: 20
    '''

    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        """Tests area of a square with side 0, expecting an area of 0."""
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_square_mul(self):
        """Tests area of a square with side 10, expecting area = 100."""
        res = area(10)
        self.assertEqual(res, 100)
    
    def test_perimeter_add(self):
        """Tests perimeter of a square with side 5, expecting perimeter = 20."""
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_large_square_area(self):
        """Tests area of a square with a very large side, expecting a correct calculation for large values."""
        res = area(10000)
        self.assertEqual(res, 100000000)

    def test_negative_perimeter(self):
        """Tests perimeter with a negative side value, expecting the product of 4 and the negative side."""
        res = perimeter(-5)
        self.assertEqual(res, -20)