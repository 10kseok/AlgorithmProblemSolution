import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    subseq = list(map(int, input().split()))
    total, count, slow, fast = 0, 0, 0, 0
    
    while True:
        if total >= M:
            total -= subseq[slow]
            slow += 1
        elif fast == N:
            break
        else:
            total += subseq[fast]
            fast += 1
        if total == M:
            count += 1
    print(count)
if __name__=="__main__":
    solution() 