from math import *

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if not ((a + b > c) & (a + c > b) & (b + c > a)):
        raise ValueError('podane liczby nie spelaniaja warunku trojkata')
    return sqrt((a+b+c) * (a+b-c) * (a-b+c) * (-a+b+c)) / 4

try:
    print(heron(5,6,4))
except ValueError:
    print('podane liczby nie spelaniaja warunku trojkata')