# 6.2
import unittest
from points import Point


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(5, 12)
        self.p2 = Point(15, 8)

    def test_str(self):
        self.assertEqual(str(self.p1), "(5, 12)")

    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point(5, 12)")

    def test_eq(self):
        self.assertTrue(self.p1 == self.p1)
        self.assertFalse(self.p1 == self.p2)

    def test_ne(self):
        self.assertFalse(self.p1 != self.p1)
        self.assertTrue(self.p1 != self.p2)

    def test_add(self):
        self.assertEqual(self.p1 + self.p1, Point(10, 24))
        self.assertEqual(self.p1 + self.p2, Point(20, 20))
        self.assertEqual(self.p2 + self.p2, Point(30, 16))

    def test_sub(self):
        self.assertEqual(self.p1 - self.p1, Point(0, 0))
        self.assertEqual(self.p1 - self.p2, Point(-10, 4))
        self.assertEqual(self.p2 - self.p1, Point(10, -4))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p1, 169)
        self.assertEqual(self.p1 * self.p2, 171)

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p1), 0)
        self.assertEqual(self.p1.cross(self.p2), -140)
        self.assertEqual(self.p2.cross(self.p1), 140)
        self.assertEqual(self.p2.cross(self.p2), 0)

    def test_length(self):
        self.assertEqual(self.p1.length(), 13)
        self.assertEqual(self.p2.length(), 17)

    def test_hash(self):
        self.assertEqual(hash(self.p1), hash((5, 12)))
        self.assertEqual(hash(self.p2), hash((15, 8)))


if __name__ == "__main__":
    unittest.main()
