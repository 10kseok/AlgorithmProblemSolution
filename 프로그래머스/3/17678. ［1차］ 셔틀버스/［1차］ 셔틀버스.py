def parseInt(time):
    splited = time.split(":")
    return int(splited[0]) * 60 + int(splited[1])
def parseTime(seconds):
    hours = seconds // 60
    hours = f'0{hours}' if hours < 10 else hours
    seconds = seconds % 60
    seconds = f'0{seconds}' if seconds < 10 else seconds
    return f'{hours}:{seconds}'

def solution(n, t, m, timetable):
    START_AT = parseInt("09:00")
    # 셔틀 버스 배차 중 가장 늦은 배차를 탄다.
    # 자리가 없으면 가장 일찍
    # 자리가 있으면 가장 늦게
    # 자리가 있는지 없는지 => 총 배차 중에서 타임 테이블에 있는 사람들 다 넣었을 때
    # 자리 배정 => 도착시각이 지금 배차 시각보다 같거나 낮다.
    timetable = sorted(timetable, key=lambda x:parseInt(x))
    shuttle_tt = [START_AT + i * t for i in range(n)]
    shuttle = [[] for i in range(n)]
    lastTimeIdx = 0
    # 다른 사람들을 다 태운다.
    # 그 중 콘이 탈 시각을 구한다. 가장 늦은 시각 = 출발 시각
    while lastTimeIdx < n and timetable:
        time = parseInt(timetable[0])
        if time <= shuttle_tt[lastTimeIdx] and len(shuttle[lastTimeIdx]) < m:
            shuttle[lastTimeIdx].append(timetable.pop(0))
        else:
            lastTimeIdx += 1
    # 자리가 날 때
    # 1, 1, 3 | 09:00 | ["08:00", "08:00"] => 09:00
    # 1, 1, 3 | 09:00 | ["09:00", "09:00"] => 08:59
    # 자리가 꽉 찼을 때
    # 1, 1, 2 | 09:00 | ["08:00", "08:00"] => 07:59
    # 1, 1, 1 | 09:00 | ["08:00", "08:00"] => 07:59
    
    # 2, 1, 2 | 09:00, 09:01 | ["08:00", "08:00"] => 07:59
    # 2, 1, 1 | 09:00, 09:01 | ["09:00", "09:00", "09:01", "09:01"] => 
    # What to know : 시간대별 빈 좌석여부
    lastShuttle = shuttle[n - 1]
    if len(lastShuttle) < m:
        return parseTime(shuttle_tt[n - 1])
    return parseTime(parseInt(lastShuttle[m - 1]) - 1)