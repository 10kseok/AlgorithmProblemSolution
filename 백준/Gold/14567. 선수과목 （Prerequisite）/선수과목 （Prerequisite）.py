from sys import stdin

input = stdin.readline

def solution(n, lectures):
    lectures.sort()
    planner = [1] * (n + 1)
    for A, B in lectures:
        planner[B] = max(planner[B], planner[A] + 1)
    
    print(*planner[1:])
    
if __name__=="__main__":
    N, M = map(int, input().split())
    lectures = [list(map(int, input().split())) for _ in range(M)]
    solution(N, lectures)