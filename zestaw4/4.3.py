def iterativeFactorial(n):
    x = 1
    for i in range(1, n+1):
        x = x * i
    return x

print(iterative_factorial(5))