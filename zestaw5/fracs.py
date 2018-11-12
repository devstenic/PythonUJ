from fractions import _gcd as gcd

def add_frac(frac1, frac2):
    result = [0, 0]
    tmp, tmp2 = [0, 0], [0,0]
    result[1] = frac1[1] * frac2[1] / gcd(frac1[1], frac2[1])
    tmp[0] = result[1] / frac1[1] * frac1[0]
    tmp2[0] = result[1] / frac2[1] * frac2[0]
    result[0] = tmp[0] + tmp2[0]
    nwd = gcd(result[0], result[1])
    result[:] = [x / nwd for x in result]
    return result


def sub_frac(frac1, frac2):
    result = [0, 0]
    tmp, tmp2 = [0, 0], [0,0]
    result[1] = frac1[1] * frac2[1] / gcd(frac1[1], frac2[1])
    tmp[0] = result[1] / frac1[1] * frac1[0]
    tmp2[0] = result[1] / frac2[1] * frac2[0]
    result[0] = tmp[0] - tmp2[0]
    nwd = gcd(result[0], result[1])
    result[:] = [x / nwd for x in result]
    return result


def mul_frac(frac1, frac2):
    result = [0, 0]
    result[0] = frac1[0] * frac2[0]
    result[1] = frac1[1] * frac2[1]
    nwd = gcd(result[0], result[1])
    result[:] = [x / nwd for x in result]
    return result


def div_frac(frac1, frac2):
    result = [0, 0]
    result[0] = frac1[0] * frac2[1]
    result[1] = frac1[1] * frac2[0]
    nwd = gcd(result[0], result[1])
    result[:] = [x / nwd for x in result]
    return result



def is_positive(frac):
    return False if (frac[0] < 0) ^ (frac[1] < 0) else True


def is_zero(frac):
    return True if frac[0] == 0 else False


def cmp_frac(frac1, frac2):
    nww = frac2[1] * frac1[1] / gcd(frac1[1], frac2[1])
    frac1[0] = (nww / frac1[1]) * frac1[0]
    frac2[0] = (nww / frac2[1]) * frac2[0]
    if frac1[0] > frac2[0]: return 1
    if frac1[0] < frac2[0]: return -1
    if frac1[0] == frac2[0]: return 0


def frac2float(frac):
    return float(frac[0]) / float(frac[1])

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])


    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 4]))
        self.assertFalse(is_zero([1, 4]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([3, 4], [4, 12]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([3, 5]), 0.6)


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy





