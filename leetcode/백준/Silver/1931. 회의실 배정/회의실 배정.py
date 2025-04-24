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
    prev_meeting = meetings[0]
    for meeting in meetings[1:]:
        if prev_meeting[END] <= meeting[START]:
            prev_meeting = meeting
            count += 1

    print(count)
solution()
