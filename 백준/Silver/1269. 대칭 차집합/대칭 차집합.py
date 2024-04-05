import sys
input = sys.stdin.readline

def solution():
    _ = input()
    A = set(input().rstrip().split()) 
    B = set(input().rstrip().split())
    A_without_B = A - B
    B_without_A = B - A
    A_without_B.update(B_without_A)
    print(len(A_without_B))
    
    
if __name__=="__main__":
    solution() 

