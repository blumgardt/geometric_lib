import unittest

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
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, 100)
    
    def test_perimeter_add(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_large_square_area(self):
        res = area(10000)
        self.assertEqual(res, 100000000)

    def test_negative_perimeter(self):
        res = perimeter(-5)
        self.assertEqual(res, -20)