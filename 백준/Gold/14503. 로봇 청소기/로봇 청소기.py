import sys
input = sys.stdin.readline
DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]
REFERENCE = 0
CLEANED = -1

def check_index(x, y):
    return 0 <= x < N and 0 <= y < M

def solution():
    global N, M
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(N)]
    answer = [0]

    def clean(r, c, d):
        while True:
            if room[r][c] == 0:
                room[r][c] = CLEANED
                answer[REFERENCE] += 1

            for _ in range(4):
                d = (d - 1) % 4
                nr, nc = r + DIRECTION[d][0], c + DIRECTION[d][1]
                if check_index(nr, nc) and room[nr][nc] == 0:
                    r, c = nr, nc
                    break
            else:
                r, c = r - DIRECTION[d][0], c - DIRECTION[d][1]
                if check_index(r, c) and room[r][c] == 1 or not check_index(r, c): 
                    print(answer[REFERENCE])
                    return
                
    clean(r, c, d)
    
if __name__=="__main__":
    solution() 
