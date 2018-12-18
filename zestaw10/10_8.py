import random


class RandomQueue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def insert(self, data):
        if self.is_full():
            raise ValueError('kolejka pełna!')
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def remove(self):
        if self.is_empty():
            raise ValueError('kolejka pusta!')
        r = random.randrange(self.head, self.tail, 1)
        data = self.items[r]
        self.items[r] = None      # usuwam referencję
        self.items = list(filter(None, self.items))
        self.tail = len(self.items)
        return data

test = RandomQueue()

test.insert(1)
test.insert(2)
test.insert(3)
test.insert(4)
test.insert(5)
print(test.remove())
