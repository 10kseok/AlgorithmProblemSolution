import sys

input = sys.stdin.readline
    
def solution():
    p, m = map(int, input().split())
    rooms = [] # [[(10, a), (15, b), ...], [(25, d), (30, e), ...] ]
    
    for _ in range(p):
        level, name = input().split()
        player = (int(level), name)
        available = False
        for room in rooms:
            if len(room) >= m:
                continue
            if player[0] - 10 <= room[0][0] <= player[0] + 10:
                available = True
                room.append(player)
                break
        if not available:
            rooms.append([player])
    
    for room in rooms:
        room.sort(key=lambda x: x[1])
        newline = '\n'
        print(f'{"Started!" if len(room) == m else "Waiting!"}\n{newline.join(list(map(lambda x:f"{x[0]} {x[1]}", room)))}')
if __name__=="__main__":
    solution() 