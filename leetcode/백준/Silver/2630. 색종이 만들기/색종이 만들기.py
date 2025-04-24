n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0

def divide(start_row, start_col, n):
    global paper, white, blue

    total = sum([
        sum(i[start_col:start_col + n])
        for i in paper[start_row:start_row + n]
    ])
    if total == 0: 
        white += 1 
        return  
    if total == n * n:
        blue += 1
        return
    
    divide(start_row, start_col, n // 2)
    divide(start_row + n // 2, start_col, n // 2)
    divide(start_row, start_col + n // 2 , n // 2)
    divide(start_row + n // 2, start_col + n // 2, n // 2)

divide(0, 0, n)
print(white, blue, sep="\n")

    
        