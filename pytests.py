import unittest
import circle
import rectangle
import square
import triangle

class UnitTestCase(unittest.TestCase):

#-------------Circle-------------

    def test_zero_mul_circle(self):
        """Tests area of a circle with radius 0, expecting an area of 0."""
        res = circle.area(0)
        self.assertEqual(res, 0)
    
    def test_negative_area_circle(self):
        """Tests area of a circle with radius -10, expecting an area of 314.159."""
        res = circle.area(-10)
        self.assertEqual(res, 314.1592653589793)
    
    def test_square_mul_circle(self):
        """Tests area of a circle with radius 4, expecting an approximate value of 50.265."""
        res = circle.area(4)
        self.assertEqual(res, 50.26548245743669)
    
    def test_perimeter_add_circle(self):
        """Tests perimeter of a circle with radius 5, expecting an approximate value of 31.416."""
        res = circle.perimeter(5)
        self.assertEqual(res, 31.41592653589793)
    
    def test_large_area_circle(self):
        """Tests perimeter of a circle with radius 50000000, expecting an approximate value of 7853981633974482.0."""
        res = circle.area(50000000)
        self.assertEqual(res, 7853981633974482.0)

#-------------Rectangle-------------
    
    def test_zero_mul_rectangle(self):
        '''Tests the area function with one side as 0, expecting an area of 0.'''
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
    
    def test_square_mul_rectangle(self):
        '''Tests the area function with equal length and width, forming a square. Expects area = side^2.'''
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)
    
    def test_perimeter_add_rectangle(self):
        '''Tests the perimeter function with typical length and width values to verify perimeter calculation.'''
        res = rectangle.perimeter(2, 5)
        self.assertEqual(res, 14)
    
    def test_negative_area_rectangle(self):
        '''Tests the area function with a negative length, expecting the result to be the product of length and width.'''
        res = rectangle.area(-3, 5)
        self.assertEqual(res, -15)

    def test_large_perimeter_rectangle(self):
        '''Tests the perimeter function with large values for length and width to verify correct handling of large inputs.'''
        res = rectangle.perimeter(100000, 50000)
        self.assertEqual(res, 300000)

#-------------Square-------------

    def test_zero_mul_square(self):
        """Tests area of a square with side 0, expecting an area of 0."""
        res = square.area(0)
        self.assertEqual(res, 0)
    
    def test_square_mul_square(self):
        """Tests area of a square with side 10, expecting area = 100."""
        res = square.area(10)
        self.assertEqual(res, 100)
    
    def test_perimeter_add_square(self):
        """Tests perimeter of a square with side 5, expecting perimeter = 20."""
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_large_square_area_square(self):
        """Tests area of a square with a very large side, expecting a correct calculation for large values."""
        res = square.area(10000)
        self.assertEqual(res, 100000000)

    def test_negative_perimeter_square(self):
        """Tests perimeter with a negative side value, expecting the product of 4 and the negative side."""
        res = square.perimeter(-5)
        self.assertEqual(res, -20)

#-------------Triangle-------------

    def test_zero_mul_triangle(self):
        """Tests area of a triangle with height 0, expecting area = 0."""
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)
    
    def test_square_mul_triangle(self):
        """Tests area of a triangle with base 10 and height 6, expecting area = 30."""
        res = triangle.area(10, 6)
        self.assertEqual(res, 30)
    
    def test_perimeter_add_triangle(self):
        """Tests perimeter of a triangle with sides 3, 5, and 4, expecting perimeter = 12."""
        res = triangle.perimeter(3, 5, 4)
        self.assertEqual(res, 12)
    
    def test_negative_area_triangle(self):
        """Tests area calculation with a negative base, expecting a negative area result if negative inputs are allowed."""
        res = triangle.area(-5, 10)
        self.assertEqual(res, -25)

    def test_large_perimeter_triangle(self):
        """Tests perimeter calculation with very large side values, ensuring no overflow errors."""
        res = triangle.perimeter(1000, 2000, 3000)
        self.assertEqual(res, 6000)