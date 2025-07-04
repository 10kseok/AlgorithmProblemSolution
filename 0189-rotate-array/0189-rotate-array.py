class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 문제
        # k번만큼 배열의 요소를 오른쪽으로 옮기기

        # 제약 조건
        # 1. 요소는 오른쪽으로만 이동
        # 2. 인덱스를 벗어난 요소는 다시 배열의 앞으로 돌아온다 (링버퍼)
        # 3. k > 0 이며 n보다 클 수 있음
        # 4. Follow up - 공간복잡도 O(1)

        # 분석
        # 1. k = n 이면 원점 복귀
        # 2. k % n만 이동시키면 k번 이동시킨 것과 같은 결과

        # 예시
        # [1 2 3] k = 3
        # [3 1 2] 1 -> (0, 1) (1, 2) (2, 3)
        # [2 3 1] 2
        # [1 2 3] 3

        # 풀이 1
        # 각 요소별 k번 이동 후의 인덱스를 구한다
        # n 이상이면 모듈러 연산 진행
        # 구한 인덱스를 통해 새로운 배열에 알맞게 채워넣는다.
        # n = len(nums)
        # k = k % n

        # shifted_indexes = [(i + k) % n for i in range(n)]
        # shifted_array = [0] * n

        # for i in range(n):
        #     shifted_array[shifted_indexes[i]] = nums[i]
        # for i in range(n):
        #     nums[i] = shifted_array[i]

        # 풀이 2
        # 1. 마지막 원소를 추출하여 맨 앞에 넣는다.
        # 2. 1번을 k번 반복한다.
        # n = len(nums)
        # k = k % n
        # for i in range(k):
        #     nums.insert(0, nums.pop())
        
        # 풀이 3
        # 1. k번 이동시 좌우 규칙 반전 발생
        # 2. 수식 0~(n-k), (n-k)~n => (n-k)~n, 0~(n-k)
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:n] + nums[:n-k]

        


        