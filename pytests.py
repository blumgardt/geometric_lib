# Import necessary modules for testing and functionality
import unittest
import math
import circle
import rectangle
import square
import triangle

# Define a test case class inheriting from unittest.TestCase
class UnitTestCase(unittest.TestCase):

    # ------------- Circle Tests -------------

    def test_circle_area_positive(self):
        """Tests area of a circle with valid radius."""
        self.assertEqual(circle.area(10), math.pi * 10**2)
        self.assertEqual(circle.area(0), 0)

    def test_circle_area_negative(self):
        """Tests area of a circle with negative radius, expecting ValueError."""
        self.assertRaises(ValueError, circle.area, -10)

    def test_circle_area_type_error(self):
        """Tests area of a circle with invalid type, expecting TypeError."""
        self.assertRaises(TypeError, circle.area, "10")

    def test_circle_perimeter_positive(self):
        """Tests perimeter of a circle with valid radius."""
        self.assertEqual(circle.perimeter(10), 2 * math.pi * 10)
        self.assertEqual(circle.perimeter(0), 0)

    def test_circle_perimeter_negative(self):
        """Tests perimeter of a circle with negative radius, expecting ValueError."""
        self.assertRaises(ValueError, circle.perimeter, -10)

    def test_circle_perimeter_type_error(self):
        """Tests perimeter of a circle with invalid type, expecting TypeError."""
        self.assertRaises(TypeError, circle.perimeter, "10")

    # ------------- Rectangle Tests -------------

    def test_rectangle_area_positive(self):
        """Tests area of a rectangle with valid sides."""
        self.assertEqual(rectangle.area(10, 5), 50)
        self.assertEqual(rectangle.area(0, 5), 0)

    def test_rectangle_area_negative(self):
        """Tests area of a rectangle with negative sides, expecting ValueError."""
        self.assertRaises(ValueError, rectangle.area, -10, 5)
        self.assertRaises(ValueError, rectangle.area, 10, -5)

    def test_rectangle_area_type_error(self):
        """Tests area of a rectangle with invalid type, expecting TypeError."""
        self.assertRaises(TypeError, rectangle.area, "10", 5)
        self.assertRaises(TypeError, rectangle.area, 10, "5")

    def test_rectangle_perimeter_positive(self):
        """Tests perimeter of a rectangle with valid sides."""
        self.assertEqual(rectangle.perimeter(10, 5), 30)

    def test_rectangle_perimeter_negative(self):
        """Tests perimeter of a rectangle with negative sides, expecting ValueError."""
        self.assertRaises(ValueError, rectangle.perimeter, -10, 5)
        self.assertRaises(ValueError, rectangle.perimeter, 10, -5)

    def test_rectangle_perimeter_type_error(self):
        """Tests perimeter of a rectangle with invalid type, expecting TypeError."""
        self.assertRaises(TypeError, rectangle.perimeter, "10", 5)
        self.assertRaises(TypeError, rectangle.perimeter, 10, "5")

    # ------------- Square Tests -------------

    def test_square_area_positive(self):
        """Tests area of a square with valid side."""
        self.assertEqual(square.area(10), 100)
        self.assertEqual(square.area(0), 0)

    def test_square_area_negative(self):
        """Tests area of a square with negative side, expecting ValueError."""
        self.assertRaises(ValueError, square.area, -10)

    def test_square_area_type_error(self):
        """Tests area of a square with invalid type, expecting TypeError."""
        self.assertRaises(TypeError, square.area, "10")

    def test_square_perimeter_positive(self):
        """Tests perimeter of a square with valid side."""
        self.assertEqual(square.perimeter(10), 40)

    def test_square_perimeter_negative(self):
        """Tests perimeter of a square with negative side, expecting ValueError."""
        self.assertRaises(ValueError, square.perimeter, -10)

    def test_square_perimeter_type_error(self):
        """Tests perimeter of a square with invalid type, expecting TypeError."""
        self.assertRaises(TypeError, square.perimeter, "10")

    # ------------- Triangle Tests -------------

    def test_triangle_area_positive(self):
        """Tests area of a triangle with valid base and height."""
        self.assertEqual(triangle.area(10, 5), 25)

    def test_triangle_area_negative(self):
        """Tests area of a triangle with negative base or height, expecting ValueError."""
        self.assertRaises(ValueError, triangle.area, -10, 5)
        self.assertRaises(ValueError, triangle.area, 10, -5)

    def test_triangle_area_type_error(self):
        """Tests area of a triangle with invalid type, expecting TypeError."""
        self.assertRaises(TypeError, triangle.area, "10", 5)
        self.assertRaises(TypeError, triangle.area, 10, "5")

    def test_triangle_perimeter_positive(self):
        """Tests perimeter of a triangle with valid sides."""
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_triangle_perimeter_negative(self):
        """Tests perimeter of a triangle with negative sides, expecting ValueError."""
        self.assertRaises(ValueError, triangle.perimeter, -3, 4, 5)
        self.assertRaises(ValueError, triangle.perimeter, 3, -4, 5)

    def test_triangle_perimeter_type_error(self):
        """Tests perimeter of a triangle with invalid type, expecting TypeError."""
        self.assertRaises(TypeError, triangle.perimeter, "3", 4, 5)
        self.assertRaises(TypeError, triangle.perimeter, 3, "4", 5)

    def test_triangle_perimeter_invalid_sides(self):
        """Tests perimeter of a triangle with invalid sides that do not form a triangle, expecting Exception."""
        self.assertRaises(Exception, triangle.perimeter, 1, 2, 4)
        self.assertRaises(Exception, triangle.perimeter, 10, 1, 2)
