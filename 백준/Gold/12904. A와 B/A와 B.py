from sys import stdin

input = stdin.readline

def solution(s, t):
    '''
    s -> t
    1. 문자열의 뒤에 A를 추가한다.
    2. 문자열을 뒤집고 뒤에 B를 추가한다.
    확인 t -> s
    '''
    s_length = len(s)
    while s_length < len(t):
        if t[-1] == 'B':
            t = t[:-1]
            t = t[::-1]
        elif t[-1] == 'A':
            t = t[:-1]
    print(1 if t == s else 0) 
            
if __name__=="__main__":
    S = input().rstrip()
    T = input().rstrip()
    solution(S, T)