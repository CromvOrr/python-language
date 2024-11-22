# 7.5
import unittest
from circles import Circle
import math


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.c1 = Circle(10, 0, 15)
        self.c2 = Circle(-10, 0, 15)
        self.c3 = Circle(25, 25, 20)

    def test_init(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, -1)

    def test_repr(self):
        self.assertEqual(repr(self.c1), "Circle(10, 0, 15)")
        self.assertEqual(repr(self.c3), "Circle(25, 25, 20)")

    def test_eq(self):
        self.assertTrue(self.c1 == self.c1)
        self.assertFalse(self.c1 == self.c2)
        self.assertFalse(self.c2 == self.c3)

    def test_ne(self):
        self.assertFalse(self.c1 != self.c1)
        self.assertTrue(self.c1 != self.c2)

    def test_area(self):
        self.assertAlmostEqual(self.c2.area(), math.pi * 225)
        self.assertAlmostEqual(self.c3.area(), math.pi * 400)

    def test_move(self):
        self.assertEqual(self.c3.move(-35, -25).pt.x, self.c2.pt.x)
        self.assertEqual(self.c3.move(-35, -25).pt.y, self.c2.pt.y)
        self.assertEqual(self.c2.move(20, 0), self.c1)

    def test_cover(self):
        self.assertEqual(self.c1.cover(self.c2), Circle(0, 0, 25))
        with self.assertRaises(ValueError):
            self.c3.cover(":/")


if __name__ == "__main__":
    unittest.main()
