from sys import stdin

input = stdin.readline

def solution(N, nums):    
    visited = [False] * (N + 1)
    answer = []
    def dfs(i, path):
        if visited[i]:
            return
        visited[i] = True
        path.append(i)
        if visited[nums[i]] and path[0] == nums[i]:
            answer.extend(path)
            return
        dfs(nums[i], path)
        if i not in answer:
            visited[i] = False
            
    for i in range(1, N + 1):
        dfs(i, [])
    
    answer.sort()
    print(len(answer))
    for ans in answer:
        print(ans)
    
if __name__=="__main__":
    N = int(input())
    nums = [0] + [int(input()) for _ in range(N)]
    solution(N, nums)

