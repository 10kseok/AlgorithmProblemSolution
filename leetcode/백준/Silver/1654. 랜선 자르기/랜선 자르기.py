from sys import stdin

input = stdin.readline

def solution(N, lan_lines):    
    lower, upper = 1, sum(lan_lines) // N
    
    while lower <= upper:
        mid = (lower + upper) // 2
        total = sum([lan // mid for lan in lan_lines])
        
        if total < N:
            upper = mid - 1
        else:
            lower = mid + 1
    print(upper)
    
if __name__=="__main__":
    K, N = map(int, input().split())
    lan_lines = [int(input()) for _ in range(K)]
    solution(N, lan_lines)
    