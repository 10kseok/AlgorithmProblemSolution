from collections import deque

n, k = map(int, input().split())
output = []
yose_deque = deque([i for i in range(1, n + 1)])

while yose_deque:
    for _ in range(k - 1):
        yose_deque.append(yose_deque.popleft())
    output.append(f'{yose_deque.popleft()}')

print(f'<{", ".join(output)}>')