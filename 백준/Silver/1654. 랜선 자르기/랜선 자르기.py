import sys
input = sys.stdin.readline

def solution():
    K, N = map(int, input().split())
    lans = [int(input()) for _ in range(K)]
    min_length, max_length = 1, max(lans)
    while min_length <= max_length:
        cutting_length = (min_length + max_length) // 2
        cnt = sum([lan // cutting_length for lan in lans])
        if cnt < N:
            max_length = cutting_length - 1
        else:
            min_length = cutting_length + 1
    print(max_length)
    
if __name__=="__main__":
    solution() 