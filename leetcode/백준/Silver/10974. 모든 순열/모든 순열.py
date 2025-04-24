import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    
    visited = [False] * (N + 1)
    answer = []
    def permutation(buffer):
        if len(buffer) == N:
            answer.append(buffer[:])
            return
        for i in range(1, N + 1):
            if not visited[i]:
                visited[i] = True
                buffer.append(i)
                permutation(buffer)
                buffer.pop()
                visited[i] = False
    permutation([])
    
    for ans in answer:
        print(*ans)

if __name__=="__main__":
    solution() 