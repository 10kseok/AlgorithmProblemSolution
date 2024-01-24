from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
input_degree = [0] + [0 for _ in range(N)]
visited = [False for _ in range(N + 1)]
output_buffer = []

for _ in range(M):
    small, tall = map(int, sys.stdin.readline().split())
    graph[small].append(tall)
    input_degree[tall] += 1

queue = deque([num for num, degree in enumerate(input_degree) if degree == 0 and num != 0])

while queue:
    student_num = queue.popleft()
    output_buffer.append(student_num)

    for next in graph[student_num]:
        input_degree[next] -= 1
        if input_degree[next] == 0:
            queue.append(next)

print(*output_buffer)
