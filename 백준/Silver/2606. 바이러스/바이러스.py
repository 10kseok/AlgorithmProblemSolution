import sys
input = sys.stdin.readline

def solution():
    global virus_cnt
    computer_cnt = int(input())
    pair_cnt = int(input())
    graph = [[] for _ in range(computer_cnt + 1)]
    for _ in range(pair_cnt):
        src, dest = map(int, input().split())
        graph[src].append(dest)
        graph[dest].append(src)
        
    visited = [False] * (computer_cnt + 1)
    visited[1] = True
    virus_cnt = 0
    def virus(src):
        global virus_cnt
        if not visited[src]:
            visited[src] = True
            virus_cnt += 1
            
        for next_computer in graph[src]:
            if not visited[next_computer]:
                virus(next_computer)
    
    virus(1)
    print(virus_cnt)
   
if __name__=="__main__":
    solution() 