import math
import unittest


L = [3,4,5,6,8,9,12,15,16]

def zamiana(L, left, right):
    tmp = L[left]
    L[left] = L[right]
    L[right] = tmp

def sort(L, left, right):
    for i in range (left + 1,right + 1):
        for j in range(left + 1, right + 1):
            if(L[j] <= L[j-1]):
                zamiana(L, j, j-1)
    return L


def mediana_sort(L, left, right):
    if len(L) == 0:
        raise ValueError("Lista jest pusta!")
    L = sort(L, left, right)
    mid = (left+right)/2
    if mid.is_integer():
        return L[int(mid)]
    else:
        x = L[int(math.floor(mid))]
        y = L[int(math.ceil(mid))]
        return (x+y)/2
    

class TestPoint(unittest.TestCase):
    def testBinarySearch(self):
        self.assertEqual(mediana_sort(L, 0, len(L) - 1), 8)

if __name__ == "__main__":
    unittest.main()