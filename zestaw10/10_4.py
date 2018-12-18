
import unittest



class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise ValueError('kolejka jest pełna!')
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise ValueError('kolejka jest pusta!')
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data


test = Queue()


test2 = Queue()

test2.put(2)
test2.put(2)
test2.put(2)
test2.put(2)
test2.put(2)


class TestQueue(unittest.TestCase):
    def test_get(self):
        with self.assertRaises(ValueError):
            test.get()
    def test_put(self):
        with self.assertRaises(ValueError):
            test2.put(3)

if __name__ == '__main__':
    unittest.main()