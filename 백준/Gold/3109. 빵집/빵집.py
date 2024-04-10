import sys
input = sys.stdin.readline

DIRECTIONS = [(-1, 1), (0, 1), (1, 1)]

# def install(r, c):
#     global board, R, C
#     board[r][c] = 'x'
#     if c == C - 1:
#         return True

#     for d in DIRECTIONS:
#         nr, nc = r + d[0], c + d[1]
#         if nr < 0 or R <= nr \
#             or board[nr][nc] == 'x':
#                 continue
                
#         if install(nr, nc):
#             return True

#     return False
    
def solution():
    global board, R, C
    R, C = map(int, input().split())
    pipeline_cnt = 0
    
    board = [list(input().strip()) for _ in range(R)]
    for r in range(R):
        install_stack = [(r, 0)]
        while install_stack:
            cur_r, cur_c = install_stack.pop()
            if cur_c == C - 1:
                pipeline_cnt += 1
                break
            board[cur_r][cur_c] = 'x'
            for d in (1, 1), (0, 1), (-1, 1):
                nr, nc = cur_r + d[0], cur_c + d[1]
                if nr < 0 or R <= nr or board[nr][nc] == 'x':
                    continue
                install_stack.append((nr, nc))
                
    # use Recursive func
    # board = [list(input().strip()) for _ in range(R)]
    # for r in range(R):
    #     if install(r, 0):
    #         pipeline_cnt += 1
            
    print(pipeline_cnt)
    
if __name__=="__main__":
    solution() 
