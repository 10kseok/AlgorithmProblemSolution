from collections import deque
import sys
input = sys.stdin.readline
DEFAULT = float('inf')

def solution():
    # input start, end
    # output 최단 시간
    # 1. 출발점부터 시작해서, 출발점의 -1, +1, *2를 탐색한다.
    # 2. 해당 지점 방문이력 저장 및 시간 저장
    # 2-1 시간 저장시, 최소값 기준으로 저장
    # 3. 모든 지점 방문시 종료
    subin, younger = map(int, input().split())
    visit_table = [DEFAULT for _ in range(100_000 + 1)]
    visit_table[subin] = 0
    
    queue = deque([subin])
    while queue:
        cur_node = queue.popleft()
        next_nodes = [cur_node - 1, cur_node + 1, cur_node * 2]
        for nn in next_nodes:
            if nn < 0 or nn > 100_000: continue
            if visit_table[nn] == DEFAULT or visit_table[nn] > visit_table[cur_node] + 1:
                visit_table[nn] = visit_table[cur_node] + 1
                queue.append(nn) 
    print(visit_table[younger])
        
if __name__=="__main__":
    solution() 


