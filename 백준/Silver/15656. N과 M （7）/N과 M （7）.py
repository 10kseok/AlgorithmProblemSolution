from sys import stdin
from itertools import product

input = stdin.readline
        
def solution(n, m):
    nums = sorted(list(map(int, input().split())))
    
    # def nCr(nums, r, buffer):
        # if r == 0:
        #     results.append(" ".join(map(str, buffer)))
        #     return

        # for i in range(len(nums)):
        #     nCr(nums, r - 1, buffer + [nums[i]])
    # results = []
    # nCr(nums, m, [])
    
    # print("\n".join(results) )
    print("\n".join(" ".join(num) for num in product(map(str, nums), repeat=m)))
if __name__=="__main__":
    N, M = map(int, input().split())
    solution(N, M)
