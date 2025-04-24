import sys

input = sys.stdin.readline

def solution():
    N, MAX_CAPACITY = map(int, input().split())
    M = int(input())
    waybills = [list(map(int, input().split())) for _ in range(M)]
    waybills.sort(key=lambda x:x[1])
    loads_per_city = [MAX_CAPACITY] * (N + 1)
    total_load_cnt = 0
    
    for src, dest, box in waybills:
        load = MAX_CAPACITY
        for i in range(src, dest):
            if load > min(loads_per_city[i], box):
                load = min(loads_per_city[i], box)
        for i in range(src, dest):
            loads_per_city[i] -= load # loading
        total_load_cnt += load # unloading
    
    print(total_load_cnt)
    
if __name__=="__main__":
    solution() 