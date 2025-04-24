import sys
input = sys.stdin.readline

def solution():
    num = input()
    
    if num.startswith('0x'):
        print(int(num, 16))
    elif num.startswith('0'):
        print(int(num[1:], 8))
    else:
        print(int(num))
    
if __name__=="__main__":
    solution() 