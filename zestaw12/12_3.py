import math
import unittest


L = [3,4,5,6,8,9,12,15,16]

def quicksort(L): 
    if len(L) <= 1:
        return L
    else:
        return quicksort([x for x in L[1:] if x < L[0]]) + \
               [L[0]] + \
               quicksort([x for x in L[1:] if x >= L[0]])
    
    
def mediana_sort(L, left, right):
    if len(L) == 0:
        raise ValueError("Lista jest pusta!")
    L = quicksort(L)
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