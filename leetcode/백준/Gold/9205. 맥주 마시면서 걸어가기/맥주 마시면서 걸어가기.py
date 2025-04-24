import sys
input = sys.stdin.readline
REGION = 20 * 50

def calculate_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def walk(home, festival, shops, visited):
    global result
    if abs(festival[0] - home[0]) + abs(festival[1] - home[1]) <= REGION:
        result = True
    else:
        for i, shp in enumerate(shops):
            if not visited[i] and calculate_distance(home, shp) <= REGION:
                visited[i] = True
                walk(shp, festival, shops, visited)
                
def solution():
    global result
    t = int(input())
    for _ in range(t):
        n = int(input())
        home = tuple(map(int, input().split()))
        shops = [tuple(map(int, input().split())) for _ in range(n)]
        visited = [False] * n
        festival = tuple(map(int, input().split()))
        result = False
        walk(home, festival, shops, visited)
        print("happy" if result else "sad")
if __name__=="__main__":
    solution() 
