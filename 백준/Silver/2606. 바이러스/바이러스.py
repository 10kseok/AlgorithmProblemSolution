import sys

N_computer = int(input())
N_pairs = int(input())

graph = [[] for _ in range(N_computer + 1)]
visited = [False] * (N_computer + 1)
count = 0

for _ in range(N_pairs):
    c1, c2 = map(int, sys.stdin.readline().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

def virus_dfs(i):
    global count
    if len(graph[i]) == 0:
        return
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            count += 1
            virus_dfs(j)

def virus_stack(i):
    global count

    stack = graph[i][:]
    while stack:
        computer = stack.pop()
        if not visited[computer]:
            visited[computer] = True
            count += 1
            stack.extend(graph[computer])

def virus_bfs(i):
    global count

    queue = graph[i][:]
    while queue:
        computer = queue.pop(0)
        if not visited[computer]:
            visited[computer] = True
            count += 1
            queue.extend(graph[computer])


virus_dfs(1); print(count)
# count = 0; visited = [False] * (N_computer + 1); visited[1] = True
# virus_stack(1); print(count)
# count = 0; visited = [False] * (N_computer + 1); visited[1] = True
# virus_bfs(1); print(count)