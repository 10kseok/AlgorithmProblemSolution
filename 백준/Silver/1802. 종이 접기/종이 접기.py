from sys import stdin

input = stdin.readline

def is_asymmetry(pattern):
    length = len(pattern)
    if length == 1:
        return True
    mid = length // 2
    return is_asymmetry(pattern[:mid]) and all(pattern[i] != pattern[length - i - 1] for i in range(mid))
        
def solution(t):
    answer = []
    for _ in range(t):
        pattern = input().rstrip()
        answer.append("YES" if is_asymmetry(pattern) else "NO")
                    
    print('\n'.join(answer))

if __name__=="__main__":
    T = int(input())
    solution(T)