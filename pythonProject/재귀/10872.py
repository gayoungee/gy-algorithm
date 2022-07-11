def factorial(x):
    res = 1
    if x > 0:
        res = x * factorial(x - 1)
    return res


n = int(input())
print(factorial(n))