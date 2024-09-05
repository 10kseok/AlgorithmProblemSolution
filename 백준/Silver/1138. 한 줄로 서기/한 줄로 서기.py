from sys import stdin

input = stdin.readline

def solution(n):
    # Default Zero
    # smaller_cnts = [0] + list(map(int, input().split()))
    # answer = [0] * (n + 1)
    
    # for i in range(1, n + 1):
    #     order = smaller_cnts[i]
    #     temp_cnt = 0
    #     for j in range(1, n + 1):
    #         if answer[j] == 0 and temp_cnt == order:
    #             answer[j] = i
    #             break
    #         elif temp_cnt < order and answer[j] == 0 or answer[j] > i:
    #             temp_cnt += 1
            
    # Default Max
    smaller_cnts = [0] + list(map(int, input().split()))
    answer = [11] * (n + 1)
    
    for i in range(1, n + 1):
        temp_cnt = 0
        for j in range(1, n + 1):
            if i < answer[j]:
                if temp_cnt == smaller_cnts[i]:
                    answer[j] = i
                    break
                temp_cnt += 1
    
    print(*answer[1:])
if __name__=="__main__":
    n = int(input())
    solution(n)