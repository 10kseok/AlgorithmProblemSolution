n = int(input())

# 1. if n == 0 then 0! = 1
# 2. n > 1 then n * fn(n - 1)
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

print(factorial(n))