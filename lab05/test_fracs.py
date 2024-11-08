# 5.2
import unittest
from fracs import *


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.f1 = [-1, 2]
        self.f2 = [1, -2]
        self.f3 = [0, 1]
        self.f4 = [0, 2]
        self.f5 = [3, 1]
        self.f6 = [6, 2]

    def test_add_frac(self):
        self.assertEqual(add_frac(self.f1, self.f2), [-1, 1])

    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.f1, self.f2), [0, 1])

    def test_mul_frac(self):
        self.assertEqual(mul_frac(self.f1, self.f2), [1, 4])

    def test_div_frac(self):
        self.assertEqual(div_frac(self.f1, self.f2), [1, 1])

    def test_is_positive(self):
        self.assertFalse(is_positive(self.zero))
        self.assertFalse(is_positive(self.f1))
        self.assertFalse(is_positive(self.f3))
        self.assertTrue(is_positive(self.f6))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero))
        self.assertFalse(is_zero(self.f1))
        self.assertFalse(is_zero(self.f5))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.f1, self.f6), -1)
        self.assertEqual(cmp_frac(self.f3, self.f4), 0)
        self.assertEqual(cmp_frac(self.f6, self.f1), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float(self.f1), -0.5)
        self.assertEqual(frac2float(self.f6), 3.0)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
