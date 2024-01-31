import sys
input = sys.stdin.readline
START, END = 0, 1

def solution():
    N = int(input())
    meetings = []

    for _ in range(N):
        start, end = map(int, input().split())
        meetings.append((start, end))
    meetings.sort(key= lambda x: (x[END], x[START]))

    count = 1
    cur_meeting = meetings[0]
    for idx in range(1, len(meetings)):
        if cur_meeting[END] <= meetings[idx][START]:
            cur_meeting = meetings[idx]
            count += 1

    print(count)
solution()
