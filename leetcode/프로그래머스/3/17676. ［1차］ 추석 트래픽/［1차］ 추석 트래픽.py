# 내 풀이
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

# 투 포인터로 개선 O(NlogN)
def solution(logs):
    # 시작 시간과 종료 시간을 저장할 리스트
    start_times = []
    end_times = []
    total_logs = len(logs)

    # 각 로그에서 시작 시간과 종료 시간 추출
    for log in logs:
        _, completion_time, process_duration = log.split()
        
        # 처리시간에서 's' 제거하고 float로 변환 (예: "2.0s" -> 2.0)
        process_duration = float(process_duration[:-1])
        
        # 완료시간을 초 단위로 변환
        hour, minute, second = completion_time.split(":")
        completion_second = int(hour) * 3600 + int(minute) * 60 + float(second)
        
        # 1초 구간의 끝점 저장 (완료시간 + 1초)
        end_times.append(completion_second + 1)
        
        # 요청의 시작 시간 저장 (완료시간 - 처리시간 + 0.001)
        # 0.001을 더하는 이유: 문제에서 시작시간을 포함한다고 명시
        start_times.append(completion_second - process_duration + 0.001)

    # 시작 시간을 기준으로 정렬
    start_times.sort()
    
    current_traffic = 0  # 현재 처리 중인 요청 수
    max_traffic = 0      # 구간 당 최대 처리량
    start_idx = 0        # 시작 시간 배열의 인덱스
    end_idx = 0          # 종료 시간 배열의 인덱스

    # 모든 시작/종료 시간을 순차적으로 처리
    while start_idx < total_logs and end_idx < total_logs:
        # 새로운 요청이 시작되는 경우
        if start_times[start_idx] < end_times[end_idx]:
            current_traffic += 1
            max_traffic = max(max_traffic, current_traffic)
            start_idx += 1
        # 진행 중인 요청이 종료되는 경우
        else:
            current_traffic -= 1
            end_idx += 1

    return max_traffic
