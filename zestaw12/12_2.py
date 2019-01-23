import unittest

L = [3,4,5,6,8,9,12,15,16]


def binary_search_recursive(L, left, right, y):

    if right < left:
        raise ValueError
    if left == right:
        if L[left] == y:
            return left
        else:
            return None

    mid = int((left + right) / 2)
    value = L[mid]
    if value == y:
        return mid
    elif value > y:
        return binary_search_recursive(L, left, mid - 1, y)
    else:
        return binary_search_recursive(L, mid + 1, right, y)


class TestPoint(unittest.TestCase):
    def testBinarySearch(self):
        self.assertEqual(binary_search_recursive(L, 0, len(L) - 1, 9), 5)

if __name__ == "__main__":
    unittest.main()