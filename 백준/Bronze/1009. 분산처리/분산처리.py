from sys import stdin

input = stdin.readline

def solution(t):
    cases = [tuple(map(int, input().split())) for _ in range(t)]
    for a, b in cases:
        if a == 1:
            print(1)
            continue
        
        digit_1 = [a % 10]
        _a = a
        for _ in range(b):
            if _a * a % 10 in digit_1:
                break
            _a = _a * a % 10
            digit_1.append(_a)
        print(10 if digit_1[b % len(digit_1) - 1] == 0 else digit_1[b % len(digit_1) - 1])
    
if __name__=="__main__":
    T = int(input())
    solution(T)