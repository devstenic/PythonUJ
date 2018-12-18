class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise ValueError('stos pełny!')
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('stos pusty!')
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data

test = Stack()

test2 = Stack()
test2.push(1)
test2.push(1)
test2.push(1)
test2.push(1)
test2.push(1)
test2.push(1)
test2.push(1)
test2.push(1)
test2.push(1)
test2.push(1)

import unittest

class TestStack(unittest.TestCase):
    def test_pop(self):
        with self.assertRaises(ValueError):
            test.pop()

    def test_push(self):
        with self.assertRaises(ValueError):
            test2.push(3)

if __name__ == '__main__':
    unittest.main()
