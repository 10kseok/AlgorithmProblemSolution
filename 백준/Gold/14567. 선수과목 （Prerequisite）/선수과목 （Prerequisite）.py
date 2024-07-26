from sys import stdin

input = stdin.readline

def solution(n, lectures):
    # Use DP
    # lectures.sort()
    # planner = [1] * (n + 1)
    # for A, B in lectures:
    #     planner[B] = max(planner[B], planner[A] + 1)
    # print(*planner[1:])
    
    # Use topology graph (no sort)
    prerequisite = [1] * (n + 1)
    topology = [[] for _ in range(n + 1)]
    for A, B in lectures:
        topology[B].append(A)
    for i in range(1, n + 1):
        if topology[i]:
            prerequisite[i] = max([prerequisite[j] for j in topology[i]]) + 1
    
    print(*prerequisite[1:])
if __name__=="__main__":
    N, M = map(int, input().split())
    lectures = [list(map(int, input().split())) for _ in range(M)]
    solution(N, lectures)