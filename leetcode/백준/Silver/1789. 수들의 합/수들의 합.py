from sys import stdin

input = stdin.readline
        
def solution(s):
    if s == 1:
        print(1)
        return
    
    n = 2
    while (n * (n + 1) >> 1) < s:
        n += 1
    print(n if (n * (n + 1) >> 1) == s else n - 1)

if __name__=="__main__":
    S = int(input())
    solution(S)