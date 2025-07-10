class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 주어진 배열로 순열을 구해라

        # 제약 조건
        # 1. 숫자는 최대 6개
        # 2. 숫자는 중복없이 -10 ~ 10

        # 문제
        # 1. 주어진 숫자를 모두 사용해서 만들 수 있는 모든 경우의 수 구해야함
        # 2. 순서에 따라 다른 경우로 취급
        # 3. 숫자가 적어서 O(n^2)도 가능

        # 풀이
        # 1. 자신을 제외한 모든 숫자로 최대 갯수(모두 사용)를 채울 때까지 경우의 수 조합
        # 2. 모든 숫자를 대상으로 1번을 진행
        # 3. 모두 사용시 정답 리스트에 추가

        n = len(nums)
        answer = []
        def _permute(nums: list[int], buffer: list[int]):
            if len(buffer) == n:
                answer.append(buffer)
            for i in range(len(nums)):
                buffer.append(nums[i])
                _permute(nums[:i] + nums[i+1:], buffer[:])
                buffer.pop()
                
        _permute(nums, [])
        return answer
