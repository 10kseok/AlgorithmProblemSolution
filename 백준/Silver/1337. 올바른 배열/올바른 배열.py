import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    array = sorted([int(input()) for _ in range(N)])
    min_needs, count, faster_idx = 4, 4, 0
    
    for idx, slower in enumerate(array) :
        count = 4
        faster_idx = idx + 1
        while faster_idx < N and slower + 4 >= array[faster_idx] and count > 0:
            faster_idx += 1
            count -= 1
        if min_needs > count:
            min_needs = count
    print(min_needs)
    
    # for idx, num in enumerate(array):
    #     nexts = [range(num, num + 5)]
    #     count = 4
    #     for n_num in array[idx:idx+5]:
    #         if n_num not in nexts:
    #             count -= 1
    #     if count < min_needs:
    #         min_needs = count
    # print(min_needs)
if __name__=="__main__":
    solution() 



