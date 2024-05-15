def parseInt(time):
    splited = time.split(":")
    return int(splited[0]) * 60 + int(splited[1])
def parseTime(seconds):
    return '%02d:%02d' % (seconds // 60, seconds % 60)

def solution(n, t, m, timetable):
    START_AT = parseInt("09:00")
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
    lastShuttle = shuttle[n - 1]
    if len(lastShuttle) < m:
        return parseTime(shuttle_tt[n - 1])
    return parseTime(parseInt(lastShuttle[m - 1]) - 1)