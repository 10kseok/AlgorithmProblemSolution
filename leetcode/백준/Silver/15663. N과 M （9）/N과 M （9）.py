from sys import stdin
from itertools import product

input = stdin.readline
        
def solution(n, m):
    nums = sorted(list(map(int, input().split())))
    
    def nCr_set(nums, r, buffer):
        if r == 0:
            results.add(buffer)
            return

        for i in range(len(nums)):
            nCr_set(nums[:i] + nums[i + 1:], r - 1, (*buffer, nums[i]))
    results = set()
    
    nCr_set(nums, m, ())
    
    results = sorted(list(results))
    for r in results:
        print(*r, sep=" ")
        
if __name__=="__main__":
    N, M = map(int, input().split())
    solution(N, M)
