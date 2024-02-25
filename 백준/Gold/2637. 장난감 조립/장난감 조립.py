import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def solution():
    N = int(input())
    M = int(input())

    indegrees = [0] * (N + 1)    
    is_base_part = [True] * (N + 1)
    reverse_part_comb_expr = defaultdict(dict)
    part_comb_expr = defaultdict(dict)
    for _ in range(M):
        result, part, count = map(int, input().split())
        part_comb_expr[result][part] = count
        reverse_part_comb_expr[part][result] = count
        is_base_part[result] = False
        indegrees[result] += 1
        
    comb_queue = deque([i for i in range(1, N + 1) if indegrees[i] == 0])
    while len(comb_queue) > 0:
        part = comb_queue.popleft()
                
        for target, cnt in reverse_part_comb_expr[part].items():
            if is_base_part[part] and part_comb_expr[target].get(part, 0) == 0:
                part_comb_expr[target][part] = cnt
            elif not is_base_part[part]:
                for p, c in part_comb_expr[part].items():
                    part_comb_expr[target][p] = part_comb_expr[target].get(p, 0) + (c * cnt)
                del part_comb_expr[target][part]
            indegrees[target] -= 1
            if indegrees[target] == 0: comb_queue.append(target)
                
    result = sorted(part_comb_expr[N])
    for p in result:
        print(p, part_comb_expr[N][p])   
    
if __name__=="__main__":
    solution()