import sys

input = sys.stdin.readline

def dfs(next, start, visit, numbers, answer):
    if not visit[numbers[next]]:
        visit[numbers[next]] = True
        dfs(numbers[next], start, visit, numbers, answer)
        visit[numbers[next]] = False
    
    if numbers[next] == start:
        answer.append(start)
    
def solution():
    N = int(input())
    numbers = [i for i in range(N + 1)]
    visit = [False] * (N + 1)
    answer = []
    for i in range(1, N + 1):
        numbers[i] =  int(input())
    for i in range(1, N + 1):
        visit[i] = True
        dfs(i, i, visit, numbers, answer)
        visit[i] = False
    
    answer.sort()
    print(len(answer))
    print(*answer, sep="\n")
    
if __name__=="__main__":
    solution() 