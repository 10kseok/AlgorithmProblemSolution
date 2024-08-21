from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = stdin.readline
        
def solution(n, m):
    workers = [[]] + [list(map(int, input().split()))[1:] for _ in range(n)]
    job = [0] * (m + 1)

    def match(worker_idx):
        for job_idx in workers[worker_idx]:
            if not job[job_idx]:
                job[job_idx] = worker_idx
                return 1
        for job_idx in workers[worker_idx]:
            if checked[job_idx]:
                continue
            checked[job_idx] = True
            if match(job[job_idx]):
                job[job_idx] = worker_idx
                return 1
        return 0
    
    answer = 0
    for i in range(1, n + 1):
        checked = [False] * (m + 1)
        answer += match(i)
        if answer == m:
            break
    print(answer)
    
if __name__=="__main__":
    N, M = map(int, input().split())
    solution(N, M)