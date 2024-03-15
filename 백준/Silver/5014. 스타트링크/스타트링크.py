from collections import deque
import sys
input = sys.stdin.readline
DEFAULT = float('inf')

def solution():
    F, S, G, U, D = map(int, input().split())
    buttons = (U, D)
    count_table = [DEFAULT for _ in range(F + 1)]
    count_table[S] = 0
    queue = deque([S])
    while queue:
        cur_floor = queue.popleft()
        next_floor = (cur_floor + buttons[0], cur_floor - buttons[1]) # up, down
        for nf in next_floor:
            if nf < 1 or F < nf: continue
            if count_table[nf] > count_table[cur_floor] + 1:
                count_table[nf] = count_table[cur_floor] + 1
                queue.append(nf)
    print("use the stairs" if count_table[G] == DEFAULT else count_table[G])
        
if __name__=="__main__":
    solution() 


