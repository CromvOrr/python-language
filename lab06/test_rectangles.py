# 6.3
import unittest
from rectangles import Rectangle
from points import Point


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(0, 0, 2, 2)
        self.r2 = Rectangle(1, 1, 7, 3)
        self.r3 = Rectangle(-1, -2, 1, 2)

    def test_str(self):
        self.assertEqual(str(self.r1), "[(0, 0), (2, 2)]")
        self.assertEqual(str(self.r2), "[(1, 1), (7, 3)]")
        self.assertEqual(str(self.r3), "[(-1, -2), (1, 2)]")

    def test_repr(self):
        self.assertEqual(repr(self.r1), "Rectangle(0, 0, 2, 2)")
        self.assertEqual(repr(self.r2), "Rectangle(1, 1, 7, 3)")
        self.assertEqual(repr(self.r3), "Rectangle(-1, -2, 1, 2)")

    def test_eq(self):
        self.assertFalse(self.r1 == self.r2)
        self.assertTrue(self.r2 == self.r2)
        self.assertFalse(self.r3 == self.r2)

    def test_ne(self):
        self.assertTrue(self.r1 != self.r2)
        self.assertFalse(self.r2 != self.r2)
        self.assertTrue(self.r3 != self.r2)

    def test_center(self):
        self.assertEqual(self.r1.center(), Point(1, 1))
        self.assertEqual(self.r2.center(), Point(4, 2))
        self.assertEqual(self.r3.center(), Point(0, 0))

    def test_area(self):
        self.assertEqual(self.r1.area(), 4)
        self.assertEqual(self.r2.area(), 12)
        self.assertEqual(self.r3.area(), 8)

    def test_move(self):
        self.r2.move(-1, -1)
        self.assertEqual(self.r2, Rectangle(0, 0, 6, 2))
        self.r3.move(1, 2)
        self.assertEqual(self.r3, Rectangle(0, 0, 2, 4))


if __name__ == "__main__":
    unittest.main()
