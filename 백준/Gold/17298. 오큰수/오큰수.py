import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    sequence = list(map(int, input().split()))
    
    answer = ['-1'] * N
    nge_stack = []
    for i in range(len(sequence) - 1, -1, -1):
        while (nge_stack and sequence[nge_stack[-1]] <= sequence[i]):
            nge_stack.pop()
        if nge_stack:
            answer[i] = f'{sequence[nge_stack[-1]]}'
        nge_stack.append(i)
    
    print(' '.join(answer))
    
if __name__=="__main__":
    solution() 

