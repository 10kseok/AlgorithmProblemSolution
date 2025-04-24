import sys

input = sys.stdin.readline

def is_puttable(box_num, rules, target):
    total_d = 0
    for r in rules:
        start, end, offset = r
        if box_num < start:
            continue
        total_d += (min(end, box_num) - start) // offset + 1
        if total_d >= target:
            return True
    return False

def solution(n, k, d):
    # Time Over
    # boxes = {}
    # for _ in range(k):
    #     start, end, offset = map(int, input().split())
    #     for box_num in range(start, end + 1, offset):
    #         boxes[box_num] = boxes.get(box_num, 0) + 1
    
    # total = 0
    # for num, cnt in sorted(boxes.items()):
    #     total += cnt
    #     if total >= d:
    #         return num
    # ----------------------
    
    # Memory Over
    # acorns = []
    # for _ in range(k):
    #     start, end, offset = map(int, input().split())
    #     for num in range(start, end + 1, offset):
    #         acorns.append(num)
    # acorns.sort()
    # return acorns[d - 1]
    # ----------------------
    
    # Binary Search
    rules = [tuple(map(int, input().split())) for _ in range(k)]
    lower, upper = min(list(map(lambda x:x[0], rules))), n
    
    while lower <= upper:
        mid = (lower + upper) // 2
        if not is_puttable(mid, rules, d):
            lower = mid + 1
        else:
            upper = mid - 1
    return lower
    
if __name__=="__main__":
    N, K, D = map(int, input().split())
    print(solution(N, K, D))

# 200 2 5
# 100 150 10
# 110 150 15