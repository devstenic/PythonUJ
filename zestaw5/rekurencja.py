def iterativeFactorial(n):
    x = 1
    for i in range(1, n+1):
        x = x * i
    return x

def fibonacci(n):
    x, y = 0, 1
    for i in range(0, n):
        x, y = y, x + y
    return x