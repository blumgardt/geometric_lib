# Import necessary modules for testing and functionality
import unittest
import circle
import rectangle
import square
import triangle

# Define a test case class inheriting from unittest.TestCase
class UnitTestCase(unittest.TestCase):

    # ------------- Circle Tests -------------
    
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
        """Tests area of a circle with a very large radius, ensuring correct computation of large values."""
        res = circle.area(50000000)
        self.assertEqual(res, 7853981633974482.0)

    # ------------- Rectangle Tests -------------
    
    def test_zero_mul_rectangle(self):
        """Tests the area of a rectangle with one side as 0, expecting an area of 0."""
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
    
    def test_square_mul_rectangle(self):
        """Tests the area of a rectangle with equal side lengths, forming a square. Expects area = side^2."""
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)
    
    def test_perimeter_add_rectangle(self):
        """Tests the perimeter of a rectangle with typical side lengths, verifying calculation correctness."""
        res = rectangle.perimeter(2, 5)
        self.assertEqual(res, 14)
    
    def test_negative_area_rectangle(self):
        """Tests the area of a rectangle with a negative side, verifying result as the product of lengths."""
        res = rectangle.area(-3, 5)
        self.assertEqual(res, -15)

    def test_large_perimeter_rectangle(self):
        """Tests the perimeter of a rectangle with very large side values, verifying handling of large inputs."""
        res = rectangle.perimeter(100000, 50000)
        self.assertEqual(res, 300000)

    # ------------- Square Tests -------------
    
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
        """Tests area of a square with a very large side, ensuring correct handling of large inputs."""
        res = square.area(10000)
        self.assertEqual(res, 100000000)

    def test_negative_perimeter_square(self):
        """Tests perimeter of a square with a negative side, expecting result as the product of 4 and the side."""
        res = square.perimeter(-5)
        self.assertEqual(res, -20)

    # ------------- Triangle Tests -------------
    
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
        """Tests area calculation with a negative base, expecting the result to follow standard area formula."""
        res = triangle.area(-5, 10)
        self.assertEqual(res, -25)

    def test_large_perimeter_triangle(self):
        """Tests perimeter calculation for a triangle with very large sides, ensuring correct computation."""
        res = triangle.perimeter(1000, 2000, 3000)
        self.assertEqual(res, 6000)
