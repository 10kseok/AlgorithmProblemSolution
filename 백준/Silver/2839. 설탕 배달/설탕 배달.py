import sys

input = sys.stdin.readline
MAX = 5000

def solution():
    # 3 ~ 5000까지 필요한 봉지 최소 갯수 입력
    N = int(input())
    min_table = [MAX for _ in range(MAX + 1)]
    min_table[3], min_table[5] = 1, 1
    # f(n) = min(f(n - 3), f(n - 5)) + 1
    for i in range(6, N + 1):
        compare_3bag, compare_5bag = i - 3, i - 5
        min_table[i] = min(min_table[compare_3bag], min_table[compare_5bag]) + 1
    print(min_table[N] if min_table[N] < MAX else -1)

if __name__=="__main__":
    solution() 