from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)
input = stdin.readline
        
def solution(t):
    # 이분 매칭
    # def dfs(req_num):
    #     for i in requests[req_num]:
    #         if checked[i]:
    #             continue
    #         checked[i] = True
    #         if not books[i] or dfs(books[i]):
    #             books[i] = req_num
    #             return True
    #     return False
    
    # for _ in range(t):
    #     n, m = map(int, input().split())
    #     requests, books, checked = [[] for _ in range(m + 1)], [0] * (n + 1), [False] * (n + 1)
    #     for i in range(1, m + 1):
    #         a, b = map(int, input().split())
    #         requests[i] = list(range(a, b + 1))
    #     answer = 0
    #     for i in range(1, m + 1):
    #         checked = [False] * (n + 1)
    #         if dfs(i):
    #             answer += 1
    #     print(answer)
    
    # 그리디 | 범위 끝으로 정렬해서 앞에서부터 채워 넣기
    for _ in range(t):
        n, m = map(int, input().split())
        visited = [False] * (n + 1)
        requests = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[1])
        answer = 0
        
        for a, b in requests:
            for i in range(a, b + 1):
                if not visited[i]:
                    visited[i] = True
                    answer += 1
                    break
        print(answer)

    # 유니온 파인드 | 최대한 뒤로 밀어내기 (=범위 끝으로 밀어넣기)
    # ...
if __name__=="__main__":
    T = int(input())
    solution(T)