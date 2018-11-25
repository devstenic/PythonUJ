from points import Point
from math import *


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promien ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return "Circle(%s,%s,%s)" % (self.pt.x, self.pt.y, self.radius)
    # "Circle(x, y, radius)"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return pi * self.radius**2
    # pole powierzchni

    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)
    # przesuniecie o (x, y)

    def cover(self, other):
        sumR = self.radius + other.radius
        subR = fabs(self.radius - other.radius)
        pointLen = hypot(other.pt.x - self.pt.x, other.pt.y - self.pt.y)
        if subR < pointLen < sumR:
            R = max(subR, sumR, pointLen)
            return Circle((self.pt.x + other.pt.x) / 2, (self.pt.y + other.pt.y) / 2, R)
        elif pointLen > sumR:
            R = (pointLen / 2) + max(self.radius, other.radius)
            return Circle((self.pt.x + other.pt.x) / 2, (self.pt.y + other.pt.y) / 2, R)
        elif pointLen < subR:
            R = max(self.radius, other.radius)
            return Circle((self.pt.x + other.pt.x) / 2, (self.pt.y + other.pt.y) / 2, R)

c = Circle(3,4,1)
print(c.cover(Circle(3,-2,4)))

    # okrąg pokrywający oba

# Kod testujący moduł.



import unittest

class TestCircle(unittest.TestCase):
    def test_eq(self):
        self.assertTrue(Circle(2, 3, 3) == Circle(4, 3, 3))
        self.assertFalse(Circle(2, 3, 4) == Circle(4, 3, 3))

    def test_ne(self):
        self.assertTrue(Circle(2,3,1) != Circle(3,2,2))
        self.assertFalse(Circle(2,3,1) != Circle(2,3, 1))

    def test_area(self):
        self.assertEqual(Circle(2, 2, 3).area(), 28.274333882308138)

    def test_move(self):
        self.assertEqual(Circle(2,3,1).move(2,2), Circle(4,5,1))

    def test_cover(self):
        self.assertEqual(Circle(3,4,1).cover(Circle(3,-2,4)), Circle(3, 1, 7) )

