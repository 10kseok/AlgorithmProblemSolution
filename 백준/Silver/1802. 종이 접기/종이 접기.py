from sys import stdin

input = stdin.readline

def is_asymmetry(pattern):
    if not pattern:
        return True
    length = len(pattern)
    mid = length // 2
    for i in range(mid):
        if pattern[i] == pattern[length - i - 1]:
            return False
    
    return is_asymmetry(pattern[:mid]) and is_asymmetry(pattern[mid + 1:])
    

def solution(t):
    answer = []
    for _ in range(t):
        pattern = input().rstrip()
        answer.append("YES" if is_asymmetry(pattern) else "NO")
                    
    print('\n'.join(answer))

if __name__=="__main__":
    T = int(input())
    solution(T)