from math import *


def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if (a == 0) & (b != 0):
        y = -c / b
        print('rozwiazaniem rownania sa pary liczb {r, ', y,'} gdzie r jest dowolne i nelezy do rzeczywistych')

    if (a != 0) & (b == 0):
        x = -c / a
        print('rozwiazaniem rownania sa pary liczb {', x, ', r} gdzie r jest dowolne i nelezy do rzeczywistych')

    if (a != 0) & (b != 0):
        print('rozwiazaniem rownania sa pary liczb {r, ', -a/b, '* r', -c/b, '} gdzie r jest dowolne i nalezy do rzeczywistych')

    print('sprzecznosc')

print(solve1(0, 0, 6))

