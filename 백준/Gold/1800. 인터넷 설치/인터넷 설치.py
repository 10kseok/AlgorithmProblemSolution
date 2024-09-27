from heapq import heappop, heappush
from sys import stdin

input = stdin.readline

def solution(n, p, k):
    cables = [[] for _ in range(n + 1)]
    for _ in range(p):
        c1, c2, cost = map(int, input().split())
        cables[c1].append((c2, cost))
        cables[c2].append((c1, cost))
    
    def can_connect_by(max_cost):
        exceed_count = [k + 1] * (n + 1)
        exceed_count[1] = 0
        queue = [(0, 1)] # cost, number
        while queue:
            c, computer = heappop(queue)
            for next_com, next_cost in cables[computer]:
                cur_exceed_count = exceed_count[computer]
                if next_cost > max_cost:
                    cur_exceed_count += 1
                if cur_exceed_count < exceed_count[next_com]:
                    exceed_count[next_com] = cur_exceed_count
                    heappush(queue, (c + next_cost, next_com))
                
        return exceed_count[n] <= k
    
    lower, upper = 0, 1_000_000
    answer = -1
    while lower <= upper:
        mid = (lower + upper) >> 1
        if can_connect_by(mid):
            answer = mid
            upper = mid - 1
        else:
            lower = mid + 1
    print(answer)
    
if __name__=="__main__":
    N, P, K = map(int, input().split())
    solution(N, P, K)