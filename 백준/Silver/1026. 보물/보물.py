from sys import stdin

input = stdin.readline
        
def solution(n, a, b):
    a, b = sorted(a), sorted(b, reverse=True)
    print(sum([a[i] * b[i] for i in range(n)]))
        
if __name__=="__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    solution(N, A, B)