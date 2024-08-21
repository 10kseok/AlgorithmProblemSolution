from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = stdin.readline
        
def solution(n, m):
    workers = [[]] + [list(map(int, input().split()))[1:] for _ in range(n)]
    job = [0] * (m + 1)
    checked = [False] * (m + 1)

    def match(worker_idx):
        for job_idx in workers[worker_idx]:
            if checked[job_idx]:
                continue
            checked[job_idx] = True
            
            if not job[job_idx] or match(job[job_idx]):
                job[job_idx] = worker_idx
                return True
        return False
    
    answer = 0
    for i in range(1, n + 1):
        if match(i):
            answer += 1
        if answer == m:
            break
        checked = [False] * (m + 1)
    print(answer)
    
if __name__=="__main__":
    N, M = map(int, input().split())
    solution(N, M)