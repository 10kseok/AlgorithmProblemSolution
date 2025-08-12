class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 주어진 간격으로 덮어씌우기
        
        # 제약 조건
        # 1. 시작값을 기준으로 오름차순 정렬 유지 필요
        # 2. 최대 원소 길이는 10,000
        # 3. 0 <= 시작 <= 끝 <= 100,000

        # 문제
        # 1. 주어진 간격으로 배열에서 알맞게 덮어씌워야함
        # 2. 만약 덮어씌우거나 병합할 요소가 없다면 그대로 위치에 맞게 원소를 삽입 필요
        # 3. 제자리 변경을 할 필요는 없고 새로 배열 생성 가능
        # 4. 두 간격이 겹친다는 것은 시작 <= 기준 끝 and 기준 시작 <= 끝을 의미함
        # 5. 여기서 말하는 기준은 전달받은 간격을 말함

        # 풀이
        # 1. 탐색 간격과 기준 간격을 비교해서 겹친다면 기준 간격을 늘린다
        # 2. 겹치지 않으면 배열에 추가한다
        #  2-1. 탐색 끝 < 기준 시작이면 탐색 간격 배열에 추가
        #  2-2. 기준 끝 < 탐색 시작이면 기준 간격 먼저 배열에 추가 후 탐색 간격 추가
        #  2-3. 기준 간격 배열 추가 후 제거하여 중복 추가 방지
        # standard_interval = newInterval[:]
        # result = []
        # START, END = 0, 1
        # for (start, end) in intervals:
        #     if not standard_interval: # 이미 기준 간격을 추가한 경우
        #         result.append([start, end])
        #         continue
            
        #     # 겹치는 경우
        #     if start <= standard_interval[END] and standard_interval[START] <= end:
        #         standard_interval[START] = min(start, standard_interval[START])
        #         standard_interval[END] = max(end, standard_interval[END])
        #     # 겹치지 않는 경우
        #     elif end < standard_interval[START]:
        #         result.append([start, end])
        #     elif standard_interval[END] < start:
        #         result.append(standard_interval)
        #         result.append([start, end])
        #         standard_interval = None

        # if standard_interval:
        #     # 모두 기준 간격으로 연결된 경우
        #     result.append(standard_interval)

        # return result

        # 풀이 2
        # 1. 기준 간격 앞에 있는 간격들을 모두 추가한다
        # 2. 기준 간격과 겹치는 간격들로부터 기준 간격의 길이를 늘리고 추가한다
        # 3. 나머지 기준 간격 뒤에 있는 간격들을 추가한다
        # intervals: List[List[int]], newInterval: List[int]
        result = []

        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1] and newInterval[0] <= intervals[i][1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1

        result.append(newInterval)
        result.extend(intervals[i:])

        return result
        