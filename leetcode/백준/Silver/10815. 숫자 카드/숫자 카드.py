import sys
input = sys.stdin.readline

def solution():
    # N = int(input())
    # sangeun = list(map(int, input().split()))
    # M = int(input())
    # numbers = list(map(int, input().split()))
    # answer = [0] * M
    
    # 시간 초과 (N^2)
    # for i in range(M):
    #     if numbers[i] in sangeun:
    #         answer[i] = 1
    
    # like Greedy
    # org_index = {num : i for i, num in enumerate(numbers)}
    # sangeun.sort()
    # numbers.sort()
    # last_search_idx = 0
    
    # for num in numbers:
    #     for i in range(last_search_idx, N):
    #         if num == sangeun[i]:
    #             answer[org_index[num]] = 1
    #             last_search_idx = i
    #             break
    #         elif num < sangeun[i]:
    #             break

    # print(*answer)
    
    # use Set Data structure
    _ = int(input())
    sangeun = set(input().split())
    _ = int(input())
    numbers = input().split()
    print(" ".join(["1" if num in sangeun else "0" for num in numbers]))
   
if __name__=="__main__":
    solution() 