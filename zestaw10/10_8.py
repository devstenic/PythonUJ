import random


class RandomQueue:

    def __init__(self, size=5):
        self.queueS = set(x for x in range(size))
        self.queueFill = set()
        self.values = size * [None]

    def insert(self, item):
        if self.is_full():
            raise Exception("Nie mozesz dodac elementu kolejka pelna!")

        x = random.sample(self.queueS, 1)[0]

        self.values[x] = item
        self.queueFill.add(x)
        self.queueS.remove(x)

    def remove(self):
        if self.is_empty():
            raise Exception("Kolejka pusta!")

        x = random.sample(self.queueFill, 1)[0]

        data = self.values[x]
        self.values[x] = None
        self.queueS.add(x)
        self.queueFill.remove(x)

        return data

    def is_empty(self):
        return len(self.queueFill) == 0

    def is_full(self):
        return len(self.queueS) == 0


test = RandomQueue()
test.insert(3)
test.insert(23)
test.insert(31)
test.insert(33)
test.insert(43)
print(test.remove())
