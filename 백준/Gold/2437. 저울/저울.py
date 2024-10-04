from sys import stdin

input = stdin.readline

def solution(n):
    # 시간 초과
    # weights = sorted(list(map(int, input().split())))
    # answer_set = set()
    # for weight in weights:
    #     buffer = set()
    #     for ans in answer_set:
    #         buffer.add(ans + weight)
    #     answer_set.update(buffer)
    #     answer_set.add(weight)
    
    # answer_set = list(answer_set)
    # for i in range(len(answer_set) - 1):
    #     if answer_set[i] + 1 < answer_set[i + 1]:
    #         print(answer_set[i] + 1)
    #         return
    # print(answer_set[-1] + 1)
    
    # 무게 범위 보장 1 ~ current_sum
    weights = sorted(list(map(int, input().split())))
    current_sum = 0    
    for weight in weights:
        if weight > current_sum + 1:
            print(current_sum + 1)
            return
        current_sum += weight
    print(current_sum + 1)
    
if __name__=="__main__":
    N = int(input())
    solution(N)