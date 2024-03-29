import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    sequence = list(map(int, input().split()))
    
    answer = [0] * N
    nge_stack = []
    for i in range(len(sequence) - 1, -1, -1):
        while (nge_stack and nge_stack[-1] <= sequence[i]):
            nge_stack.pop()
        answer[i] = nge_stack[-1] if nge_stack else -1
        nge_stack.append(sequence[i])
    
    print(*answer)
    
if __name__=="__main__":
    solution()