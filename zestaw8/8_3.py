import random
from math import *

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    inCircle = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if hypot(x, y) <= 1:
            inCircle += 1
    liczbaPI = 4 * inCircle/n
    return liczbaPI

print(calc_pi())
print(calc_pi(1000))
print(calc_pi(10000))
print(calc_pi(100000))
print(calc_pi(1000000))
