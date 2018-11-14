import unittest
import math


class Point:

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __repr__(self):
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other):
        x = bool(self.x == other.x and self.y == other.y)
        return bool

    def __ne__(self, other):
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return float(self.x * other.x + self.y * other.y)

    # v1 * v2, iloczyn skalarny
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return float(math.sqrt(self.x * self.x + self.y * self.y))


class TestPoint(unittest.TestCase):
    def testStr(self):
        self.assertEqual(str(Point(4, 1)), "(4, 1)")

    def testRepr(self):
        self.assertEqual(repr(Point(3, 3)), "Point(3, 3)")

    def testEq(self):
        self.assertTrue(Point(4, 4) == Point(4, 4))

    def testNe(self):
        self.assertFalse(Point(1, 2).__ne__(Point(1, 2)), True)

    def testAdd(self):
        self.assertEqual(Point(1, 1) + Point(2, 0), Point(3, 1))

    def testSub(self):
        self.assertEqual(Point(10, 13) - Point(2, 2), Point(8, 11))

    def testMul(self):
        self.assertEqual(Point(2, 1) * Point(3, 3), 9.0)

    def testCross(self):
        self.assertEqual(Point(2, 2).cross(Point(2, 2)), 0)

    def testLength(self):
        self.assertEqual(Point(3, 4).length(), 5)


if __name__ == "__main__":
    unittest.main()
