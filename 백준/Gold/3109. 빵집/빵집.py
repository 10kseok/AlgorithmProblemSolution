from collections import deque
import sys
input = sys.stdin.readline

DIRECTIONS = [(-1, 1), (0, 1), (1, 1)]

def solution():
    R, C = map(int, input().split())
    board = [input().strip() for _ in range(R)]
    pipeline_cnt = 0
    installed = [[False] * C for _ in range(R)]
    
    for r in range(R):
        install_stack = [(r, 0)]
        while install_stack:
            cur_r, cur_c = install_stack.pop()
            if cur_c == C - 1:
                pipeline_cnt += 1
                break
            installed[cur_r][cur_c] = True
            for d in DIRECTIONS[::-1]:
                nr, nc = cur_r + d[0], cur_c + d[1]
                if nr < 0 or R <= nr or nc < 0 or C <= nc \
                    or board[nr][nc] == 'x' \
                    or installed[nr][nc]:
                    continue
                install_stack.append((nr, nc))
        
    print(pipeline_cnt)
    
if __name__=="__main__":
    solution() 
