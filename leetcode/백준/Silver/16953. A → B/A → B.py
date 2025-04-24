from sys import stdin

input = stdin.readline
        
def solution(a, b):
    # Use BFS
    # from collections import deque
    # queue = deque([b])
    # cnt = 0
    # while queue:
    #     num = queue.popleft()
    #     if num == a:
    #         print(cnt + 1)
    #         return
    #     elif num < a:
    #         continue
        
    #     if num % 2 == 0:
    #         converted = num // 2
    #     elif num % 10 == 1:
    #         converted = (num - 1) // 10
    #     else:
    #         continue
    #     queue.append(converted)
    #     cnt += 1
    # print(-1)
    
    # Use DFS
    def dfs(num, cnt):
        if num == a:
            print(cnt + 1)
            return
        elif num < a:
            print(-1)
            return
        
        if num % 2 == 0:
            dfs(num // 2, cnt + 1)
        elif num % 10 == 1:
            dfs((num - 1) // 10, cnt + 1)
        else:
            print(-1)
    dfs(b, 0)
if __name__=="__main__":
    A, B = map(int, input().split())
    solution(A, B)
    
# 3 4
# => -1

# 2 11
# => -1

# 2 182
# => -1

# 2 23
# => -1