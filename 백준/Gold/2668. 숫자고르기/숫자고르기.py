from sys import stdin

input = stdin.readline

def solution(N, nums):    
    answer = []
    def dfs(i, start):
        visited[i] = True
        _next = nums[i]
        if not visited[_next]:
            dfs(_next, start)
            return
        if start == _next:
            answer.append(_next)
            
    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        dfs(i, i)
    
    answer.sort()
    print(len(answer))
    for ans in answer:
        print(ans)
    
if __name__=="__main__":
    N = int(input())
    nums = [0] + [int(input()) for _ in range(N)]
    solution(N, nums)
