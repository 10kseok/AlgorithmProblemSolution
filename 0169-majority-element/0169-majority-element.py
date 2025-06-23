class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 최빈수를 구해야함
        # 1. 나타나는 숫자별로 빈도수를 구한다.
        # 2. 그 중 가장 높은 수를 가지는 숫자를 반환한다.
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        max_num, max_value = None, 0
        for num, count in counter.items():
            if count > max_value:
                max_value = count
                max_num = num

        return max_num