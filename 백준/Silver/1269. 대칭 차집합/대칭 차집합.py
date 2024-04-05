import sys
input = sys.stdin.readline

def solution():
    a, b = map(int, input().split())
    A = set(input().rstrip().split()) 
    B = set(input().rstrip().split())
    A_without_B = A - B
    common = a - len(A_without_B)
    print(a + b - 2 * common)
    
if __name__=="__main__":
    solution() 