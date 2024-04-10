from collections import deque
import sys
input = sys.stdin.readline
MAX_CONVERT = 10_000

def solution():
    prime_table = [True] * 10_000
    prime_table[0], prime_table[1], prime_table[2], prime_table[3] = False, False, True, True
    THOUSAND = 1000
    for i in range(2, int(10_000 ** 0.5)):
        for j in range(i + i, 10_000, i):
            prime_table[j] = False
            
    T = int(input())
    answer = []
    for _ in range(T):
        src, dest = map(int, input().split())
        
        route = {prime_num : MAX_CONVERT for prime_num in range(1000, 10000) if prime_table[prime_num]}
        route[src] = 0
        convert_Q = deque([src])
        while convert_Q:
            num = convert_Q.popleft()
            # after
            for d in range(4):
                digit = 10**d # level of number
                target_num = num // digit % 10
                base_num = num - target_num * digit
                for i in range(0, 10):
                    if i == 0 and digit == THOUSAND or target_num == i:
                        continue
                    next_num = base_num + i * digit
                    if prime_table[next_num] and route.get(next_num) > route[num] + 1:
                        route[next_num] = route[num] + 1
                        convert_Q.append(next_num)
            
            # before
            # # 천의 자리
            # for i in range(1, 10):
            #     next_num = f'{i}{num[1:]}'
            #     if next_num == num:
            #         continue
            #     if prime_table[int(next_num)] and route.get(next_num) > route[num] + 1:
            #         route[next_num] = route[num] + 1
            #         convert_Q.append(next_num)
            # # 백의 자리
            # for i in range(0, 10):
            #     next_num = f'{num[0]}{i}{num[2:]}'
            #     if next_num == num:
            #         continue
            #     if prime_table[int(next_num)] and route.get(next_num) > route[num] + 1:
            #         route[next_num] = route[num] + 1
            #         convert_Q.append(next_num)
            # # 십의 자리
            # for i in range(0, 10):
            #     next_num = f'{num[:2]}{i}{num[3]}'
            #     if next_num == num:
            #         continue
            #     if prime_table[int(next_num)] and route.get(next_num) > route[num] + 1:
            #         route[next_num] = route[num] + 1
            #         convert_Q.append(next_num)
            # # 일의 자리
            # for i in range(0, 10):
            #     next_num = f'{num[:3]}{i}'
            #     if next_num == num:
            #         continue
            #     if prime_table[int(next_num)] and route.get(next_num) > route[num] + 1:
            #         route[next_num] = route[num] + 1
            #         convert_Q.append(next_num)
            
        answer.append(f'{route[dest]}' if route[dest] != MAX_CONVERT else "Impossible")
    print('\n'.join(answer))
if __name__=="__main__":
    solution() 
