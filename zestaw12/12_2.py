import unittest

L = [3,4,5,6,8,9,12,15,16]


def binary_search_recursive(L, left, right=0, y=None):
    if y is None:
        y = len(L) - 1
    if right > y:
        return False

    mid = (right + y) // 2
    if left == L[mid]:
        return mid
    if left < L[mid]:
        return binary_search_recursive(L, left, right, mid-1)
    # left > L[mid]
    return binary_search_recursive(L, left, mid+1, y)



class TestPoint(unittest.TestCase):
    def testBinarySearch(self):
        self.assertEqual(binary_search_recursive(L, 12), 6)

if __name__ == "__main__":
    unittest.main()