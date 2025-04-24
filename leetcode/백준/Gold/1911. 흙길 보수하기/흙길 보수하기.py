import sys
input = sys.stdin.readline

def solution():
    N, L = map(int, input().split())
    total_plank_cnt = 0
    waters = [list(map(int, input().split())) for _ in range(N)]
    waters.sort()
    
    last_plank_pos = 0
    for start, end in waters:
        start = max(start, last_plank_pos)
        w_length = end - start
        planks = -(-w_length // L) 
        total_plank_cnt += planks
        last_plank_pos = start + L * planks
    
    print(total_plank_cnt)

if __name__=="__main__":
    solution() 

# 3 1
# 1 2
# 2 3
# 3 4

# 3 10
# 1 2
# 2 3
# 3 4 

