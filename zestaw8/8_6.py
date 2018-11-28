import time
import math


# programowanie dynamicznie
def pd(i, j):
    if i == 0:
        return 1.0
    elif j == 0:
        return 0.0
    else:
        value = d.get((i, j))
        if (value != None):
            return value
        else:
            value = 0.5 * (pd(i - 1, j) + pd(i, j - 1))
            d[(i, j)] = value
            return value


d = {(0, 0): 0.5, (0, 1): 1.0, (1, 0): 0.0}


# rekurencyjne
def p(i, j):
    if (j < 0) or (i < 0):
        raise ValueError("Ujemna wartosc argumentu!")
    if i == 0 and j == 0:
        return 0.5
    elif i == 0:
        return 1.0
    elif j == 0:
        return 0.0
    else:
        return 0.5 * (p(i - 1, j) + p(i, j - 1))


def porownanie(i, j):
    start = time.perf_counter()
    vpd = str(pd(i, j))
    tpd = time.perf_counter() - start

    start = time.perf_counter()
    vp = str(p(i, j))
    tp = time.perf_counter() - start

    print('dynamiczne: obliczenia:', vpd, 'czas: ', tpd)
    print('rekurencyne: obliczenia:', vp, 'czas: ', tp)



porownanie(11, 13)
