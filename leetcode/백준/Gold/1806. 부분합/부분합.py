from sys import stdin

input = stdin.readline
        
def solution(n, s):
    sequence = list(map(int, input().split()))
    left, right, total = 0, 0, sequence[0]
    answer = n + 1
    
    while left <= right and right < n:
        if total < s and right + 1 < n:
            right += 1
            total += sequence[right]
        elif total >= s:
            if answer > right - left + 1:
                answer = right - left + 1
            total -= sequence[left]
            left += 1
        else:
            left += 1
    
    print(answer if answer != n + 1 else 0)

if __name__=="__main__":
    N, M = map(int, input().split())
    solution(N, M)
