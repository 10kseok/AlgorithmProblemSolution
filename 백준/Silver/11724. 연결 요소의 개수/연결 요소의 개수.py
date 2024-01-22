import sys
    
# 각 자료구조별 특징
# 인접 행렬 -> 연결된 노드들을 찾아서 계산해줘야함 -> 행렬로 인한 공간 복잡도 상승
# 인접 리스트 -> 연결된 노드들을 번호순으로 계속 정렬해줘야함 -> 코드가 훨씬 적어짐.

N, M = map(int, input().split())
graph = [[] * (N + 1) for _ in range(N + 1)]
parent = [i for i in range(0, N + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    smaller = find(v1)
    larger = find(v2)   
    parent[max(smaller, larger)] = min(smaller, larger)

for i in range(1, N + 1):
    find(i)

print(len(set(parent[1:])))

