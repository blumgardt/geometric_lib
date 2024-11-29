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
        """Tests area of a circle with valid radius using subTest."""
        test_cases = [
            (10, math.pi * 10**2),
            (0, 0),
        ]
        for radius, expected in test_cases:
            with self.subTest(radius=radius):
                self.assertEqual(circle.area(radius), expected)

    def test_circle_area_negative(self):
        """Tests area of a circle with negative radius, expecting ValueError."""
        test_cases = [-10, -20, -30]
        for radius in test_cases:
            with self.subTest(radius=radius):
                self.assertRaises(ValueError, circle.area, radius)

    def test_circle_area_type_error(self):
        """Tests area of a circle with invalid type, expecting TypeError."""
        test_cases = ["10", None, [10]]
        for radius in test_cases:
            with self.subTest(radius=radius):
                self.assertRaises(TypeError, circle.area, radius)

    def test_circle_perimeter_positive(self):
        """Tests perimeter of a circle with valid radius using subTest."""
        test_cases = [
            (10, 2 * math.pi * 10),
            (0, 0),
        ]
        for radius, expected in test_cases:
            with self.subTest(radius=radius):
                self.assertEqual(circle.perimeter(radius), expected)

    def test_circle_perimeter_negative(self):
        """Tests perimeter of a circle with negative radius, expecting ValueError."""
        test_cases = [-10, -15]
        for radius in test_cases:
            with self.subTest(radius=radius):
                self.assertRaises(ValueError, circle.perimeter, radius)

    def test_circle_perimeter_type_error(self):
        """Tests perimeter of a circle with invalid type, expecting TypeError."""
        test_cases = ["10", None, [10]]
        for radius in test_cases:
            with self.subTest(radius=radius):
                self.assertRaises(TypeError, circle.perimeter, radius)

    # ------------- Rectangle Tests -------------

    def test_rectangle_area_positive(self):
        """Tests area of a rectangle with valid sides using subTest."""
        test_cases = [
            ((10, 5), 0),
            ((0, 5), 0),
        ]
        for (length, width), expected in test_cases:
            with self.subTest(length=length, width=width):
                self.assertEqual(rectangle.area(length, width), expected)

    def test_rectangle_area_negative(self):
        """Tests area of a rectangle with negative sides, expecting ValueError."""
        test_cases = [(-10, 5), (10, -5), (-10, -5)]
        for length, width in test_cases:
            with self.subTest(length=length, width=width):
                self.assertRaises(ValueError, rectangle.area, length, width)

    def test_rectangle_area_type_error(self):
        """Tests area of a rectangle with invalid type, expecting TypeError."""
        test_cases = [("10", 50), (10, "5"), (None, 5)]
        for length, width in test_cases:
            with self.subTest(length=length, width=width):
                self.assertRaises(TypeError, rectangle.area, length, width)

    def test_rectangle_perimeter_positive(self):
        """Tests perimeter of a rectangle with valid sides using subTest."""
        test_cases = [
            ((10, 5), 30)
        ]
        for (length, width), expected in test_cases:
            with self.subTest(length=length, width=width):
                self.assertEqual(rectangle.perimeter(length, width), expected)

    def test_rectangle_perimeter_negative(self):
        """Tests perimeter of a rectangle with negative sides, expecting ValueError."""
        test_cases = [(-10, 5), (10, -5), (-10, -5)]
        for length, width in test_cases:
            with self.subTest(length=length, width=width):
                self.assertRaises(ValueError, rectangle.perimeter, length, width)

    def test_rectangle_perimeter_type_error(self):
        """Tests perimeter of a rectangle with invalid type, expecting TypeError."""
        test_cases = [("10", 5), (10, "5"), (None, 5)]
        for length, width in test_cases:
            with self.subTest(length=length, width=width):
                self.assertRaises(TypeError, rectangle.perimeter, length, width)

    # ------------- Square Tests -------------

    def test_square_area_positive(self):
        """Tests area of a square with valid side using subTest."""
        test_cases = [
            (10, 100),
            (0, 0),
        ]
        for side, expected in test_cases:
            with self.subTest(side=side):
                self.assertEqual(square.area(side), expected)

    def test_square_area_negative(self):
        """Tests area of a square with negative side, expecting ValueError."""
        test_cases = [-10, -20]
        for side in test_cases:
            with self.subTest(side=side):
                self.assertRaises(ValueError, square.area, side)

    def test_square_area_type_error(self):
        """Tests area of a square with invalid type, expecting TypeError."""
        test_cases = ["10", None, [10]]
        for side in test_cases:
            with self.subTest(side=side):
                self.assertRaises(TypeError, square.area, side)

    def test_square_perimeter_positive(self):
        """Tests perimeter of a square with valid side using subTest."""
        test_cases = [
            (10, 40),
            (0, 0),
        ]
        for side, expected in test_cases:
            with self.subTest(side=side):
                self.assertEqual(square.perimeter(side), expected)

    def test_square_perimeter_negative(self):
        """Tests perimeter of a square with negative side, expecting ValueError."""
        test_cases = [-10, -20]
        for side in test_cases:
            with self.subTest(side=side):
                self.assertRaises(ValueError, square.perimeter, side)

    def test_square_perimeter_type_error(self):
        """Tests perimeter of a square with invalid type, expecting TypeError."""
        test_cases = ["10", None, [10]]
        for side in test_cases:
            with self.subTest(side=side):
                self.assertRaises(TypeError, square.perimeter, side)

    # ------------- Triangle Tests -------------

    def test_triangle_area_positive(self):
        """Tests area of a triangle with valid base and height using subTest."""
        test_cases = [
            ((10, 5), 25),
            ((0, 5), 0),
        ]
        for (base, height), expected in test_cases:
            with self.subTest(base=base, height=height):
                self.assertEqual(triangle.area(base, height), expected)

    def test_triangle_area_negative(self):
        """Tests area of a triangle with negative base or height, expecting ValueError."""
        test_cases = [(-10, 5), (10, -5), (-10, -5)]
        for base, height in test_cases:
            with self.subTest(base=base, height=height):
                self.assertRaises(ValueError, triangle.area, base, height)

    def test_triangle_area_type_error(self):
        """Tests area of a triangle with invalid type, expecting TypeError."""
        test_cases = [("10", 5), (10, "5"), (None, 5)]
        for base, height in test_cases:
            with self.subTest(base=base, height=height):
                self.assertRaises(TypeError, triangle.area, base, height)

    def test_triangle_perimeter_positive(self):
        """Tests perimeter of a triangle with valid sides using subTest."""
        test_cases = [
            ((3, 4, 5), 12),
        ]
        for (a, b, c), expected in test_cases:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(triangle.perimeter(a, b, c), expected)

    def test_triangle_perimeter_negative(self):
        """Tests perimeter of a triangle with negative sides, expecting ValueError."""
        test_cases = [(-3, 4, 5), (3, -4, 5), (3, 4, -5)]
        for a, b, c in test_cases:
            with self.subTest(a=a, b=b, c=c):
                self.assertRaises(ValueError, triangle.perimeter, a, b, c)

    def test_triangle_perimeter_type_error(self):
        """Tests perimeter of a triangle with invalid type, expecting TypeError."""
        test_cases = [("3", 4, 5), (3, "4", 5), (None, 4, 5)]
        for a, b, c in test_cases:
            with self.subTest(a=a, b=b, c=c):
                self.assertRaises(TypeError, triangle.perimeter, a, b, c)

    def test_triangle_perimeter_invalid_sides(self):
        """Tests perimeter of a triangle with invalid sides that do not form a triangle, expecting Exception."""
        test_cases = [(1, 2, 4), (10, 1, 2)]
        for a, b, c in test_cases:
            with self.subTest(a=a, b=b, c=c):
                self.assertRaises(Exception, triangle.perimeter, a, b, c)
