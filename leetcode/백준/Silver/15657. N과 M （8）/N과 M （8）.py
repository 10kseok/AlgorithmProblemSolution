from sys import stdin
from itertools import product

input = stdin.readline
        
def solution(n, m):
    nums = sorted(list(map(int, input().split())))
    
    def nCr_including_self_num(nums, r, buffer):
        if r == 0:
            results.append(" ".join(map(str, buffer)))
            return

        for i in range(len(nums)):
            nCr_including_self_num(nums[i:], r - 1, buffer + [nums[i]])
    results = []
    nCr_including_self_num(nums, m, [])
    
    print("\n".join(results) )
if __name__=="__main__":
    N, M = map(int, input().split())
    solution(N, M)
