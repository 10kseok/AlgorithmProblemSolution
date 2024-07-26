from sys import stdin

input = stdin.readline

def solution(positions):
    positions.sort()
    
    line_start = positions[0][0]
    line_end = positions[0][1]
    length = line_end - line_start
    for x, y in positions[1:]:
        if x <= line_end < y:
            length += y - line_end
            line_end = y
        elif line_end < x:
            line_start, line_end = x, y
            length += line_end - line_start
    print(length)
        
if __name__=="__main__":
    N = int(input())
    positions = [list(map(int, input().split())) for _ in range(N)]
    solution(positions)