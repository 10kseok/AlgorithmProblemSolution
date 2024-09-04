from sys import stdin

input = stdin.readline

def flip(matrix, row_idx, col_idx):
    for i in range(row_idx, row_idx + 3):
        for j in range(col_idx, col_idx + 3):
            matrix[i][j] = '0' if matrix[i][j] == '1' else '1'

def is_equal(n, matrix_a, matrix_b):
    for i in range(n):
        if matrix_a[i] != matrix_b[i]:
            return False
    return True

def solution(n, m):
    A = [list(input().strip()) for _ in range(n)]
    B = [list(input().strip()) for _ in range(n)]
    
    cnt = 0
    for i in range(n - 2):
        for j in range(m - 2):
            if A[i][j] != B[i][j]:
                flip(A, i, j)
                cnt += 1
                
    print(cnt if is_equal(n, A, B) else -1)
    
if __name__=="__main__":
    n, m = map(int, input().split())
    solution(n, m)