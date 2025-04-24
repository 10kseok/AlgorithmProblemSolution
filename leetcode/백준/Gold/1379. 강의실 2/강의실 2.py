import heapq
import sys
input = sys.stdin.readline
END_TIME, ROOM_NUM = 0, 3

def solution():
    N = int(input())
    lectures = [list(map(int, input().split())) for _ in range(N)] # 강의실 번호, 시작 시각, 종료 시각
    room_nums = [0] * (N + 1)
    rooms = []
    lectures.sort(key= lambda x:(x[1], x[2])) # 시작 시각 기준 정렬

    room_num = 1
    lecture_num, start, end = lectures[0]
    room_nums[lecture_num] = room_num

    heapq.heappush(rooms, (end, start, lecture_num, room_num))
    for lecture in lectures[1:]:
        lecture_num, start, end = lecture
        
        if start >= rooms[0][END_TIME]:
            available = heapq.heappop(rooms)
            heapq.heappush(rooms, (end, start, lecture_num, available[ROOM_NUM]))
            room_nums[lecture_num] = available[ROOM_NUM]
        else:
            room_num += 1
            heapq.heappush(rooms, (end, start, lecture_num, room_num))
            room_nums[lecture_num] = room_num

    print(len(rooms))
    print(*room_nums[1:], sep="\n")

if __name__=="__main__":
    solution()