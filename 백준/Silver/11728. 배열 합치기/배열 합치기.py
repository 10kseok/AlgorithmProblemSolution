import sys
input = sys.stdin.readline

def solution():
    input()
    a = input()
    b = input()
    print(" ".join(sorted((a + b).split(), key=int)))
    
if __name__=="__main__":
    solution() 

