import sys
from collections import deque

input = sys.stdin.readline

def solution(N, K):
    num_length, k = len(N), int(K)
    swapped_nums_per_k = { i:set(['-1']) for i in range(1, k + 1) }
    
    Q = deque([(N, 0)])
    while Q:
        num, cnt = Q.popleft()
        if cnt == k:
            break
        for i in range(num_length):
            for j in range(i + 1, num_length):
                swapped = f'{num[:i]}{num[j]}{num[i + 1:j]}{num[i]}{num[j + 1:]}'
                if i == 0 and num[i] != '0' and num[j] == '0':
                    continue
                if swapped not in swapped_nums_per_k[cnt + 1]:
                    swapped_nums_per_k[cnt + 1].add(swapped)
                    Q.append((swapped, cnt + 1))  
                    
    return max(swapped_nums_per_k[k])
if __name__=="__main__":
    N, K = input().split()
    print(solution(N, K))

# 정렬하듯이 교환하면 생기는 문제 case
# 381993 3
# wrong : 381993 -> 981933 -> 991833 -> 998133
# right : 381993 -> 981393 -> 991383 -> 998313
