from sys import stdin

input = stdin.readline

def solution(n):
    positions = [list(map(int, input().split())) for _ in range(n)]
    positions.sort()
    
    line_end = positions[0][1]
    length = line_end - positions[0][0]
    for x, y in positions[1:]:
        if y <= line_end:
            continue
        if x <= line_end:
            length += max(y - line_end, 0)
        else:
            length += y - x
        line_end = y
    print(length)
        
if __name__=="__main__":
    N = int(input())
    solution(N)