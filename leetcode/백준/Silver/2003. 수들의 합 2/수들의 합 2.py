import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    subseq = list(map(int, input().split()))
    total, count, slow, fast = 0, 0, 0, 0
    
    total += subseq[slow]
    for slow in range(N):
        while fast < N - 1 and total < M:
            fast += 1
            total += subseq[fast]
        if total == M:
            count += 1
        total -= subseq[slow]
    print(count)
    
if __name__=="__main__":
    solution() 