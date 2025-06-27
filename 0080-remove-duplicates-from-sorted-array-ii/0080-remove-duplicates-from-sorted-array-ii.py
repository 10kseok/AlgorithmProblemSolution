class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 두번까지만 중복을 허용하면서 그 외에 중복은 제거

        # 제약조건
        # 1. 오름차순
        # 2. 제거된 후에도 오름차순 유지 필요
        # 3. 추가적인 배열 할당 금지, 공간 복잡도 O(1)

        # 문제
        # 1. 세번이상 중복되는 경우 발생
        # 2. 중복 = 현재 기준 앞 또는 뒤에 같은 숫자가 있다
        # 3. 이러한 경우(중복)가 2번이상 발생하면 제거해야함
        # 4. 남겨진 숫자 갯수 반환
        
        # 풀이 1 (실패)
        # 1. 세 개의 수를 비교한다.
        # 2. 첫번째 수, 두번째 수, 세번째 수 모두 같으면 세번째 수를 제거한다.
        #     2-1. 세번째 수와 다른 숫자를 찾는다.
        #     2-2. 그 수와 세번째 수의 자리를 바꾼다.
        #     2-3. 바뀐 위치부터 탐색을 이어나간다.
        # 3. 세 개의 수 중 하나라도 다르면 다음 위치로 넘어가 다시 1번부터 진행한다.
        # --> 바뀐 위치에 사이에 끼인 값이 변경되지 않아 실패
        '''
        n = len(nums)
        if n < 3:
            return n

        k = 2
        while k < n:
            if sum(nums[k - 2:k+1]) // 3 == nums[k]:
                next_idx = k + 1
                while next_idx < n and nums[k] == nums[next_idx]:
                    next_idx += 1
                if next_idx >= n:
                    return k
                nums[k], nums[next_idx] = nums[next_idx], nums[k]
                k = next_idx
            else:
                k += 1

        return k
        '''

        # 풀이 2 (예제 1 커버 실패)
        # 1. 현재 숫자와 2번째전 숫자와 비교한다.
        # 2. 같으면 3번 중복된 것임으로 해당 위치를 저장하고 숫자를 제거할(덮어쓸) 다음 숫자를 탐색한다
        # 3. 다른 숫자를 찾으면 중복되었던 위치에 덮어쓴다.
        '''
        n = len(nums)
        if n < 3:
            return n

        k = 2
        for i in range(2, n):
            if nums[i] == nums[i - 2]:
                continue
            else:
                nums[k] = nums[i]
                k += 1

        return k
        '''

        # 풀이 3
        # 1. 앞에서부터 중복 2개이 두개가 넘지 않도록 숫자들을 채워나간다.
        # 2. 결국 뒤에 있는 숫자를 앞으로 당겨와야 한다.
        # 3. 그러니 중복이 2개가 되지 않는다면 뒤에 숫자를 앞으로 당겨온다.
        # 4. (i < n) nums[i - 2] != nums[i] = 중복 2개 아님을 보장
        n = len(nums)
        if n < 3:
            return n

        k = 2
        for i in range(2, n):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k






        