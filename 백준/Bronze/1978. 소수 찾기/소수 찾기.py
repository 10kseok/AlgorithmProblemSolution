n = int(input())
numbers = list(map(int, input().split()))

for num in numbers:
    if num == 1:
        n -= 1

    for j in range(2, num):
        if num % j == 0:
            n -= 1
            break
print(n)