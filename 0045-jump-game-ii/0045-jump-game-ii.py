class Solution:
    def jump(self, nums: List[int]) -> int:
        # 처음부터 연속으로 점프해서 마지막 원소에 도착하는 최소 점프 횟수를 구해라

        # 제약 조건
        # 1. 점프는 배열 안으로 한정된다 (j = 최대 점프 횟수, i + j < n and 0 <= j <= nums[i])
        # 2. 각 요소에는 최대 점프 가능 횟수가 나타난다
        # 3. 마지막 요소에 도착하는 경로는 반드시 존재한다

        # 문제
        # 1. 점프하는 횟수가 적으면서 마지막 요소에 도착해야한다
        # 2. 선택할 수 있는 요소는 현재 인덱스의 점프 횟수 값으로 한정된다.
        # 3. 최대한 한번에 점프를 많이 할 수 있는 선택지를 골라야한다.

        # 풀이 1(그리디)
        # 1. 점프 후 점프 횟수(j) 범위내에 가장 큰 값을 찾는다.
        # 2. 탐색 범위 끝에서 가장 큰 값의 인덱스와 거리 차이를 구해 추가 탐색 범위를 구한다. 
        # 3. 탐색 범위가 추가되면 점프 횟수를 증가한다.
        # * 탐색한 최대값이 최소 횟수를 보장하지 않아 실패 *
        # -> [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3] 

        # n = len(nums)
        # if n == 1:
        #     return 0

        # jump_count = 1
        # stop = 0 + nums[0]
        # max_jump = 0
        # max_jump_idx = 0

        # for i in range(1, n - 1):
        #     if max_jump <= nums[i]:
        #         max_jump = nums[i]
        #         max_jump_idx = i
        #     if i == stop:
        #         stop += max_jump - (i - max_jump_idx)
        #         jump_count += 1
        #         max_jump = 0
            
        # return jump_count

        # 풀이 2
        # 1. 각 인덱스별로 도착할 수 있는 최소 점프 횟수를 저장한다.
        # 2. 점프 횟수 범위 내에서 현재 점프 인덱스에서의 최소 점프 횟수 + 1과 지금 점프 횟수를 비교한다.
        # 3. 최소 점프 횟수만을 남긴다.
        # n = len(nums)
        # min_jumps = [float('inf')] * n
        # min_jumps[0] = 0

        # for i in range(n):
        #     edge = min(i + 1 + nums[i], n)
        #     for j in range(i + 1, edge):
        #         min_jumps[j] = min(min_jumps[j], min_jumps[i] + 1)

        # return min_jumps[n - 1]

        # 풀이 3 올바른 그리디 
        # 1. 각 점프 횟수별로 가장 멀리 갈 수 있는 위치를 찾는다
        # 2. 가장 멀리 갈 수 있는 위치에서 다음 점프를 진행한다.
        jump = 0
        cur_end = 0
        farthest = 0
        n = len(nums)

        if n == 1:
            return 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:
                cur_end = farthest
                jump += 1
                if cur_end >= n - 1:
                    break
        return jump


