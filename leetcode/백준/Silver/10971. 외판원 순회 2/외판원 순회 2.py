n = int(input())
total_cost = float("inf")
graph = [list(map(int, input().split())) for _ in range(n)]

def traversal(dep, path, cost):
    global total_cost
    if len(path) > n + 1:
        return
    if len(path) > 0 and path[0] == dep:
        total_cost = min(cost, total_cost)
        return
    
    for next in range(n):
        if graph[dep][next] == 0: continue
        if next not in path \
            or (len(path) == n - 1 and path[0] == next) \
            and cost < total_cost:
            path.append(dep)
            traversal(next, path[:], cost + graph[dep][next])
            path.pop()

traversal(0, [], 0)

print(total_cost)