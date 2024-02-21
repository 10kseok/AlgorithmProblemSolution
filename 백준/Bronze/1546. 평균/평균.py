import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    scores = list(map(int, input().split()))
    max_score = max(scores)
    print(sum(scores) / max_score / N * 100)

if __name__=="__main__":
    solution()