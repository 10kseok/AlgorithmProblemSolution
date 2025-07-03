class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 각 인덱스의 최대 점프 횟수를 사용해서 마지막 인덱스 도착 가능 여부 판단

        # 제약 조건
        # 1. 배열 길이 최대 10_000
        # 2. 최대 점프 100_000번 가능
        # 3. 주어진 점프 횟수는 최대 점프 횟수 내에서 가능

        # 문제
        # 1. 각 요소의 점프 횟수를 이용해서 마지막 인덱스에 도착 가능한 경우를 찾아야함
        # 2. 만약 가능한 경우가 없다면 false 판단 가능하면 true 반환

        # 풀이 1
        # 1. 마지막 인덱스부터 순회를 시작한다
        # 2. 해당 인덱스가 마지막 인덱스로부터 도달 가능한 인덱스인지 판단
        # 3. 마지막 인덱스로부터 떨어진 거리보다 최대 점프 횟수가 같거나 크면, 기준점을 해당 인덱스로 변경
        # 4. 그렇지 않으면 그대로 순회
        # 5. 기준점을 바꾼 인덱스에는 진입 가능 표시
        # 6. 마지막까지 순회후 첫번째 인덱스에 진입 가능 표시로 도달 여부 반환

        # Case 1  
        #   [2, 3, 1, 1, 4]
        # 1. -  -  -  o  -
        # 2. -  -  o  o  -
        # 3. -  o  o  o  -
        # 4. o  o  o  o  -
        # Case 2
        #   [3, 2, 1, 0, 4]
        # 1. -  -  -  -  -
        # 1. x  x  x  x  -

        n = len(nums)
        if n < 2:
            return True

        target = n - 1
        availables = [False] * n
        for i in range(n - 2, -1, -1):
            if target - i <= nums[i]:
                target = i
                availables[i] = True
        return availables[0]
