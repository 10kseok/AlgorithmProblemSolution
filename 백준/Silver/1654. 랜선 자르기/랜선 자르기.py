import sys
input = sys.stdin.readline

def solution():
    K, N = map(int, input().split())
    lans = [int(input()) for _ in range(K)]
    min_length, max_length = 1, max(lans)
    last_cutting_length = 1
    while min_length <= max_length:
        cutting_length = (min_length + max_length) // 2
        cnt = 0
        for lan in lans:
            cnt += lan // cutting_length
        if cnt < N:
            max_length = cutting_length - 1
        else:
            last_cutting_length = cutting_length
            min_length = cutting_length + 1
    print(last_cutting_length)

if __name__=="__main__":
    solution() 