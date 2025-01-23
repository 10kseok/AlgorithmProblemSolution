# def solution(lines):
#     answer = 0
    
#     def get_time_milis(s: str) -> int:
#         """
#         ex)
#         s = 01:00:04.002
#         """
#         hours, minutes, seconds = s.split(":")
#         seconds, miliseconds = map(int, seconds.split("."))
#         return (int(hours) * 3600 + int(minutes) * 60 + seconds) * 1000 + miliseconds
    
#     def get_start_time_milis(s: str, t: str) -> int:
#         """
#         ex)
#         s = 01:00:04.002
#         t = 2.0s
#         """
#         t_miliseconds = float(t[:-1]) * 1000
#         return get_time_milis(s) - t_miliseconds + 1
    
#     max_throughput = 0
#     MAX_T = 3000
#     lines_s_t_only = [line.split()[1:] for line in lines]
    
#     for i in range(len(lines_s_t_only)):
#         s, t = lines_s_t_only[i]
#         end_time_milis = get_time_milis(s) + 999
#         throughput = 1
#         for j in range(i + 1, len(lines_s_t_only)):
#             next_s, next_t = lines_s_t_only[j]
#             if get_start_time_milis(next_s, next_t) <= end_time_milis:
#                 throughput += 1
#             elif get_time_milis(next_s) - end_time_milis > 3000:
#                 break
#         if max_throughput < throughput:
#             max_throughput = throughput
        
#     return max_throughput

# 다른 사람 풀이 (좋아요 1등)
def solution(lines) : 

    S, E = [] , []
    totalLines = 0 
    for line in lines : 
        totalLines += 1 
        (d,s,t) = line.split()

        t = float(t[0:-1])
        (hh,mm,ss) = s.split(":")
        seconds = int(hh) * 3600 + int(mm) * 60 + float(ss)

        E.append(seconds+1)
        S.append(seconds - t + 0.001)


    S.sort()

    curTraffic = 0 
    maxTraffic = 0 
    countE = 0 
    countS = 0

    while (countE < totalLines) and (countS < totalLines) :
        if S[countS] < E[countE] : 
            curTraffic += 1 
            maxTraffic = max(maxTraffic, curTraffic)
            countS += 1 
        else :
            curTraffic -= 1 
            countE += 1 

    return maxTraffic