from sys import stdin

input = stdin.readline

def solution(n, k):
    # N * N 개의 수 중에서 K번째 수를 찾아내야함.
    # N이 최대 10만이기에 효율을 생각해야하는 문제. (N * N = 100억)
    # 데이터 형태가 B = [1, 2, 3, ... 1 * N, 2, 4, 6, ... 2 * N, ... N * N)
    def count_latter_nums(num):
        return sum(min(n, num // i) for i in range(1, n + 1))

    lower, upper = 1, k
    while lower <= upper:
        num = (lower + upper) >> 1
        if count_latter_nums(num) >= k:
            answer = num
            upper = num - 1            
        else:
            lower = num + 1
    
    print(answer)
            
if __name__=="__main__":
    N = int(input())
    K = int(input())
    solution(N, K)