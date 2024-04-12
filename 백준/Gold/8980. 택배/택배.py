from collections import deque
import sys
input = sys.stdin.readline

def solution():
    N, MAX_CAPACITY = map(int, input().split())
    M = int(input())
    load_Q = [list(map(int, input().split())) for _ in range(M)]
    load_Q.sort()
    load_Q = deque(load_Q)
    unload_table = [0] * (N + 1)
    cur_capa, total_delivery_cnt = MAX_CAPACITY, 0
    for i in range(1, N + 1):
        if unload_table[i]: # unload
            total_delivery_cnt += unload_table[i]
            cur_capa += unload_table[i]
            unload_table[i] = 0
            
        while load_Q:
            src, dest, cnt = load_Q.popleft()
            if src != i:
                load_Q.appendleft([src, dest, cnt])
                break
            
            if cur_capa == 0:
                break
                
            if src == i: # load
                load = cnt
                if cur_capa < load:
                    load = cur_capa
                cur_capa -= load
                unload_table[dest] += load
                
    print(total_delivery_cnt)
            
if __name__=="__main__":
    solution() 