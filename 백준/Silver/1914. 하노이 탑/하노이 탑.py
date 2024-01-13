n = int(input())

def hanoi(n, start, target):
    if n > 1: hanoi(n - 1, start=start, target=6 - start - target)
    print(start, target)
    if n > 1: hanoi(n - 1, start=6 - start - target, target=target)

print(2 ** n - 1)
if (n <= 20): hanoi(n, 1, 3)
