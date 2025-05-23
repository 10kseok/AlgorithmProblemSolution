from sys import stdin

input = stdin.readline
        
def solution(n):
    # Use Deque
    # from collections import deque
    # sequences = deque(sorted([int(input()) for _ in range(n)]))
    # total = 0 
    # while sequences:
    #     if sequences[-1] > 0:
    #         num = sequences.pop()
    #         if sequences and sequences[-1] > 0:
    #             num2 = sequences.pop()
    #             total += max(num + num2, num * num2)
    #         else:
    #             total += num
    #     else:
    #         num = sequences.popleft()
    #         if sequences:
    #             num2 = sequences.popleft()
    #             total += max(num + num2, num * num2)
    #         else:
    #             total += num
    # print(total)
    
    # Use index
    sequences = sorted([int(input()) for _ in range(n)])
    total, left, right = 0, 0, n - 1
    while left <= right:
        if sequences[right] > 0:
            num = sequences[right]
            right -= 1
            if right >= 0 and sequences[right] > 0:
                num2 = sequences[right]
                right -= 1
                total += max(num + num2, num * num2)
            else:
                total += num
        else:
            num = sequences[left]
            left += 1
            if left <= right:
                num2 = sequences[left]
                left += 1
                total += max(num + num2, num * num2)
            else:
                total += num
    print(total)
    
if __name__=="__main__":
    n = int(input())
    solution(n)