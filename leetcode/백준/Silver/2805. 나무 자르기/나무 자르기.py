import sys

N, M = map(int, input().split())
heights = list(map(int, sys.stdin.readline().split()))

lower = 0
upper = max(heights)

while lower <= upper:
    total_tree = 0
    cutting_height = (lower + upper) // 2
    for h in heights:
        if h <= cutting_height: continue
        if total_tree > M: break
        total_tree += (h - cutting_height)

    if total_tree >= M:
        # 필요량 초과시 절단 높이 증가
        lower = cutting_height + 1
    elif total_tree < M:
        # 필요량 부족시 절단 높이 감소
        upper = cutting_height - 1

print(upper)


