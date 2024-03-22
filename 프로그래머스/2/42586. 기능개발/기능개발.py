from math import ceil

def solution(progresses, speeds):
    answer = []
    max_work_day, i, count = ceil((100 - progresses[0]) / speeds[0]), 0, 1

    while i < len(progresses) - 1:
        next_prgr = ceil((100 - progresses[i + 1]) / speeds[i + 1])
        if max_work_day < next_prgr:
            answer.append(count)
            count = 1
            max_work_day = next_prgr
        else:
            count += 1
        i += 1
        
    answer.append(count)
    return answer