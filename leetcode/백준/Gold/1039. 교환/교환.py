import sys
from itertools import combinations

input = sys.stdin.readline

def solution(N, K):
    num_length = len(N)
    if num_length == 1 or num_length == 2 and N[-1] == '0':
        return -1
    
    buffer = [tuple(N)]
    swap_combs = list(combinations(range(num_length), 2))
    for _ in range(int(K)):
        answer_set = set()
        for num in buffer:
            for i, j in swap_combs:
                separated_num = list(num)
                separated_num[i], separated_num[j] = separated_num[j], separated_num[i]
                answer_set.add(tuple(separated_num))
        buffer = list(answer_set)[:]
    
    return ''.join(max(answer_set))
if __name__=="__main__":
    N, K = input().split()
    print(solution(N, K))

# 정렬하듯이 교환하면 생기는 문제 case
# 381993 3
# wrong : 381993 -> 981933 -> 991833 -> 998133
# right : 381993 -> 981393 -> 991383 -> 998313
