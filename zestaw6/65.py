from fractions import _gcd as gcd


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
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
        f = 'Frac(' + str(self.x) + ', ' + str(self.y) + ')'
        return f

    # zwraca "Frac(x, y)"

    def __add__(self, other):
        nfrac = Frac()
        nfrac.y = (self.y * other.y) / gcd(self.y, other.y)
        tmp = nfrac.y / self.y * self.x
        tmp2 = nfrac.y / other.y * other.x
        nfrac.x = tmp + tmp2
        nwd = gcd(nfrac.x, nfrac.y)
        nfrac.x /= nwd
        nfrac.y /= nwd
        return nfrac

    # frac1 + frac2

    def __sub__(self, other):
        nfrac = Frac()
        nfrac.y = (self.y * other.y) / gcd(self.y, other.y)
        tmp = nfrac.y / self.y * self.x
        tmp2 = nfrac.y / other.y * other.x
        nfrac.x = tmp - tmp2
        nwd = gcd(nfrac.x, nfrac.y)
        nfrac.x /= nwd
        nfrac.y /= nwd
        return nfrac

    # frac1 - frac2

    def __mul__(self, other):
        nfrac = Frac()
        nfrac.x = self.x * other.x
        nfrac.y = self.y * other.y
        nwd = gcd(nfrac.x, nfrac.y)
        nfrac.x /= nwd
        nfrac.y /= nwd
        return nfrac

    # frac1 * frac2

    def __div__(self, other):
        nfrac = Frac()
        nfrac.x = self.x * other.y
        nfrac.y = self.y * other.x
        nwd = gcd(nfrac.x, nfrac.y)
        nfrac.x /= nwd
        nfrac.y /= nwd
        return nfrac

    # frac1 / frac2

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __cmp__(self, other):
        nww = (other.y * self.y) / gcd(self.y, other.y)
        self.x = (nww / self.y) * self.x
        other.x = (nww / other.y) * other.x
        if self.x > other.x: return 1
        if self.x < other.x: return -1
        if self.x == other.x: return 0

    # cmp(frac1, frac2)

    def __float__(self):
        return float(self.x) / float(self.y)
    # float(frac)


import unittest


class TestFrac(unittest.TestCase):
    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(Frac(2, 3)), '2/3')

    def test_repr(self):
        self.assertEqual(str(Frac(4, 3)), 'Frac(4, 3)')

    def test_add(self):
        self.assertEqual(Frac(2, 4) + Frac(3, 5), Frac(22, 20))

    def test_sub(self):
        self.assertEqual(Frac(2, 3) - Frac(3, 4), Frac(-1, 12))

    def test_mul(self):
        self.assertEqual(Frac(3, 8) * Frac(6, 4), Frac(18, 32))

    def test_div(self):
        self.assertEqual(Frac(2, 3) / Frac(3, 5), Frac(10, 9))

    def test_neg(self):
        self.assertEqual(-Frac(3, 2), Frac(-3, 2))

    def test_invert(self):
        self.assertEqual(~Frac(4, 5), Frac(5, 4))

    def test_cmp(self):
        self.assertEqual(Frac(3, 4), Frac(2, 3), 1)

    def test_float(self):
        self.assertEqual(float(Frac(3, 5)), 0.6)


if __name__ == '__main__':
    unittest.main()

