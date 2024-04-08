import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    
    for num in range(1, N):
        option_sum = sum(map(int, f'{num}'))
        if num + option_sum == N:
            print(num)
            return
    print(0)    
if __name__=="__main__":
    solution() 

