import sys
input = sys.stdin.readline

def solution():
    answer = list(map(int, input().split()))
    print(answer[0] + answer[1])
    
if __name__=="__main__":
    solution() 