N = int(input())

count = 0
board = [0] * N

def is_promissing(row_idx):   
    for i in range(row_idx):
        # 위에서부터 퀸을 놔두기에 row 값 판별은 제외
        # 상하 or 대각선 겹치는지 확인
        # i - row_idx = x 값의 차 (row 번호 차이)
        # board[i] - board[row_idx] = y 값의 차 (col 번호 차이)
        if board[i] == board[row_idx] or (abs(board[i] - board[row_idx]) == abs(i - row_idx)):
            return False
    return True

def search_queen(row):
    global count

    if row == N:
        count += 1
        return
    for col in range(N):
        # 한 행에 퀸 한개를 놓을 수 있다. = 모든 열을 확인해본다.
        # 만약 놓을 수 없다면 탐색이 지속되지 않는다.
        board[row] = col
        # 해당 열에 퀸을 놓을 수 있으면 탐색 지속
        if is_promissing(row):
            search_queen(row + 1)

search_queen(0)
print(count)