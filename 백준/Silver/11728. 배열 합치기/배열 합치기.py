import sys
input = sys.stdin.readline

def solution():
    input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    print(*sorted(a + b), sep=" ")
    
    
if __name__=="__main__":
    solution() 

