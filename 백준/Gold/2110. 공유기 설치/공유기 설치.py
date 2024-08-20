from sys import stdin

input = stdin.readline
        
def solution(n, m):
    # 목표: 가장 가까운 공유기의 최대값!
    homes = sorted([int(input()) for _ in range(n)])
    
    def is_available(min_distance):
        # 맨 앞에는 항상 공유기는 설치
        # -> 맨 앞에 공유기가 없으면 젤 첫번째 공유기 설치시 앞에 간격을 구할 수가 없다
        # -> 간격은 공유기와 공유기 간에 간격이기 때문
        slow, fast = 0, 1
        cnt = 1
        while slow < n and fast < n and cnt < m:
            if homes[fast] - homes[slow] < min_distance:
                fast += 1
                continue
            cnt += 1
            slow = fast
            fast = slow + 1
        return cnt >= m
      
    # lower = 작은 쪽이 항상 조건을 만족하는 쪽
    lower, upper = 1, homes[-1] - homes[0]
    while lower <= upper:
        mid = (lower + upper) >> 1
        if is_available(mid):
            lower = mid + 1
        else:
            upper = mid - 1
    print(upper)
    
if __name__=="__main__":
    N, M = map(int, input().split())
    solution(N, M)
