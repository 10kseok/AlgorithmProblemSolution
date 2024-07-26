from sys import stdin

input = stdin.readline

def solution(n):
    positions = [list(map(int, input().split())) for _ in range(n)]
    positions.sort()
    
    line_start = positions[0][0]
    line_end = positions[0][1]
    length = line_end - line_start
    for x, y in positions[1:]:
        if y <= line_end:
            continue
        if x <= line_end:
            length += y - line_end
            line_end = y
        else:
            line_start, line_end = x, y
            length += line_end - line_start
    print(length)
        
if __name__=="__main__":
    N = int(input())
    solution(N)