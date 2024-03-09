import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    table = [0] + list(map(int, input().split()))
    for i in range(1, N + 1):
        table[i] = table[i] + table[i - 1]
    
    result = []
    for _ in range(M):
        start, end = map(int, input().split())
        result.append(table[end] - table[start - 1])
    print(*result, sep="\n")
    

if __name__=="__main__":
    solution() 