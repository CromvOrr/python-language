# 5.2
from math import gcd


def simplify(frac):
    num, den = frac
    if den == 0:
        raise ValueError("Error: Denominator cannot be zero")
    _gcd = gcd(abs(num), abs(den))
    num = num // _gcd
    den = den // _gcd
    if den < 0:
        num, den = -num, -den
    return [num, den]


def add_frac(frac1, frac2):
    num = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    den = frac1[1] * frac2[1]
    return simplify([num, den])


def sub_frac(frac1, frac2):
    num = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    den = frac1[1] * frac2[1]
    return simplify([num, den])


def mul_frac(frac1, frac2):
    num = frac1[0] * frac2[0]
    den = frac1[1] * frac2[1]
    return simplify([num, den])


def div_frac(frac1, frac2):
    if frac2[0] == 0:
        raise ValueError("Error: Denominator cannot be zero")
    num = frac1[0] * frac2[1]
    den = frac1[1] * frac2[0]
    return simplify([num, den])


def is_positive(frac):
    return frac[0] * frac[1] > 0


def is_zero(frac):
    return frac[0] == 0


def cmp_frac(frac1, frac2):
    diff = sub_frac(frac1, frac2)
    if diff[0] > 0:
        return 1
    elif diff[0] < 0:
        return -1
    else:
        return 0


def frac2float(frac):
    return frac[0] / frac[1]
