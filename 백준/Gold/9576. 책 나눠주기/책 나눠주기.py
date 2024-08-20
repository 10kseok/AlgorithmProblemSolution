from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

input = stdin.readline
        
def solution(t):
    def dfs(req_num):
        for i in requests[req_num]:
            if checked[i]:
                continue
            checked[i] = True
            if not books[i] or dfs(books[i]):
                books[i] = req_num
                return True
        return False
    
    for _ in range(t):
        n, m = map(int, input().split())
        requests, books, checked = [[] for _ in range(m + 1)], [0] * (n + 1), [False] * (n + 1)
        for i in range(1, m + 1):
            a, b = map(int, input().split())
            requests[i] = list(range(a, b + 1))
        answer = 0
        for i in range(1, m + 1):
            checked = [False] * (n + 1)
            if dfs(i):
                answer += 1
        print(answer)
        
if __name__=="__main__":
    T = int(input())
    solution(T)