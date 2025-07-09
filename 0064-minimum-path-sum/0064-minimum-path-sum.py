class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 경로의 최소합 구하기

        # 제약 조건
        # 1. 양수만 존재
        # 2. 오른쪽 또는 아래로만 한칸씩 이동 가능
        # 3. m(행), n(열) <= 200 으로 최대 200 x 200이 가능

        # 문제
        # 1. mxn 크기의 배열에서 최종 목표 도달시 최소 경로 합을 구해야함
        # 2. 오른쪽 또는 아래로만 이동해서 최종 목표에 도달해야함

        # 풀이
        # 1. 각 왼쪽과 위쪽 값중 최소값을 구한다
        # 2. 현재 값에 앞에서 구한 최소값을 더해 갱신한다

        DIRECTION = [(0, -1), (-1, 0)] # LEFT, UP
        MAX_VALUE = float('inf')
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                min_prev = MAX_VALUE
                for (di, dj) in DIRECTION:
                    prev_i = i + di
                    prev_j = j + dj
                    if prev_i < 0 or prev_i >= m or prev_j < 0 or prev_j >= n:
                        continue
                    min_prev = min(min_prev, grid[prev_i][prev_j]) 
                grid[i][j] += min_prev if min_prev != MAX_VALUE else 0
        
        return grid[m - 1][n - 1]