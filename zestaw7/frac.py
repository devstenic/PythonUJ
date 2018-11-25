from fractions import *

class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        if y == 0:
            raise ValueError('Dzielenie przez 0!')
        self.x = x
        self.y = y

    def __str__(self):
        if self.y == 1:
            return str(self.x)
        else:
            b = str(self.x) + '/' + str(self.y)
            return b
    # zwraca "x/y" lub "x" dla y=1

    def __repr__(self):
        return 'Frac(' + str(self.x) + ', ' + str(self.y) + ')'
    # zwraca "Frac(x, y)"

    def __cmp__(self, other):
        s = float(self)
        o = float(other)

        if(s < o):
            return -1
        if(s == o):
            return 0
        if(s > o):
            return 1
    # porównywanie

    def __add__(self, other):
        if type(other) is int:
            other = Frac(other)

        if type(other) is float:
            other = Frac(*other.as_integer_ratio())

        y = (self.y * other.y) / gcd(self.y, other.y)
        tmp = y / self.y * self.x
        tmp2 = y / other.y * other.x
        x = tmp + tmp2
        nwd = gcd(x, y)
        x /= nwd
        y /= nwd
        nfrac = Frac(x, y)
        return nfrac

    # frac1+frac2, frac+int

    __radd__ = __add__              # int+frac

    def __sub__(self, other):
        if type(other) is int:
            other = Frac(other)

        if type(other) is float:
            other = Frac(*other.as_integer_ratio())

        y = (self.y * other.y) / gcd(self.y, other.y)
        tmp = y / self.y * self.x
        tmp2 = y / other.y * other.x
        x = tmp - tmp2
        nwd = gcd(x, y)
        x /= nwd
        y /= nwd
        nfrac = Frac(x, y)
        return nfrac
        # frac1-frac2, frac-int

    def __rsub__(self, other):# int-frac # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        if type(other) is int:
            other = Frac(other)

        if type(other) is float:
            other = Frac(*other.as_integer_ratio())

        x = self.x * other.x
        y = self.y * other.y

        nwd = gcd(x, y)
        x /= nwd
        y /= nwd
        nfrac = Frac(x, y)
        return nfrac
    # frac1*frac2, frac*int

    __rmul__ = __mul__              # int*frac

    def __div__(self, other):
        if type(other) is int:
            other = Frac(other)

        if type(other) is float:
            other = Frac(*other.as_integer_ratio())

        x = self.x * other.y
        y = self.y * other.x

        nwd = gcd(x, y)
        x /= nwd
        y /= nwd
        nfrac = Frac(x, y)
        return nfrac
    # frac1/frac2, frac/int

    def __rdiv__(self, other):
        x = self.y * other
        y = self.x * other
        nwd = gcd(x, y)
        x /= nwd
        y /= nwd
        nfrac = Frac(x, y)
        return nfrac
    # int/frac

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    # -frac = (-1)*frac

    def __invert__(self):
        return Frac(self.y, self.x)
    # odwrotnosc: ~frac

    def __float__(self):
        return float(self.x) / float(self.y)
    # float(frac)

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Frac(2, 3)), '2/3')
        self.assertEqual(str(Frac(2, 1)), '2')

    def test_repr(self):
        self.assertEqual(repr(Frac(4, 3)), 'Frac(4, 3)')

    def test_add(self):
        self.assertEqual(Frac(2, 4) + Frac(3, 5), Frac(11, 10))
        self.assertEqual(Frac(2, 4) + 1, Frac(3, 2))
        self.assertEqual(1 + Frac(2, 4), Frac(3, 2))
        self.assertEqual(1.5 + Frac(2, 4), Frac(1, 2))

    def test_sub(self):
        self.assertEqual(Frac(2, 3) - Frac(3, 4), Frac(-1, 12))
        self.assertEqual(Frac(2, 3) - 1, Frac(-1, 3))
        self.assertEqual(1 - Frac(2, 3), Frac(1, 3))
        self.assertEqual(1.5 - Frac(2, 3), Frac(5, 6))
        self.assertEqual(Frac(2, 3) - 1.5, Frac(-5, 6))

    def test_mul(self):
        self.assertEqual(Frac(3, 2) * Frac(3, 2), Frac(9, 4))
        self.assertEqual(Frac(2, 3) * 2, Frac(4, 3))
        self.assertEqual(2 * Frac(1, 3), Frac(2, 3))

        self.assertEqual(Frac(2, 3) * 1.5, 1)
        self.assertEqual(3.5 * Frac(1, 2), Frac(7, 4))

    def test_div(self):
        self.assertEqual(Frac(5, 4) / Frac(1, 2), Frac(5, 2))
        self.assertEqual(Frac(1, 3) / 2, Frac(1, 6))
        self.assertEqual(2 / Frac(2, 3), 3)

        self.assertEqual(Frac(3, 2) / 1.5, 1)
        self.assertEqual(3.5 / Frac(1, 2), 7)

    def test_neg(self):
        self.assertEqual(-Frac(3, 2), Frac(-3, 2))

    def test_invert(self):
        self.assertEqual(~Frac(4, 5), Frac(5, 4))

    def test_cmp(self):
        self.assertTrue(Frac(3, 4) > Frac(2, 3))
        self.assertTrue(Frac(2, 3) < Frac(3, 4))
        self.assertTrue(Frac(2, 3) == Frac(4, 6))
        self.assertFalse(Frac(2, 3) == Frac(4, 5))

    def test_float(self):
        self.assertEqual(float(Frac(3, 5)), 0.6)