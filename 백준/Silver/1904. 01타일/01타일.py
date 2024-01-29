import sys

a, b = 0, 1
N = int(sys.stdin.readline())
for _ in range(N):
    a, b = b % 15746, (a + b) % 15746
print(b)

