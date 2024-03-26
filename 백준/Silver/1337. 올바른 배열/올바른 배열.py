import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    array = sorted([int(input()) for _ in range(N)])
    min_needs = 4
    
    for idx, num in enumerate(array):
        nexts = [i for i in range(num, num + 5)]
        count = 4
        for n_num in array[idx+1:idx+5]:
            if n_num in nexts:
                count -= 1
        if count < min_needs:
            min_needs = count
    print(min_needs)
if __name__=="__main__":
    solution() 