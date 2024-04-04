import sys
input = sys.stdin.readline

def solution():
    num = int(input())
    divider = 2

    while divider <= num:
        while num % divider == 0:
            num /= divider
            print(divider)
        divider += 1
    
if __name__=="__main__":
    solution() 

