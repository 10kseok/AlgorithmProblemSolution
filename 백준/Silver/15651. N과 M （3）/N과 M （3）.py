from sys import stdin

input = stdin.readline
        
def solution(n, m):
    nums = [i for i in range(1, n + 1)]
    results = []
    
    def choose(_nums, r, buffer):
        # if r == 0:
        #     results.append(buffer)
        #     return
        
        # for i in range(len(_nums)):
        #     buffer.append(_nums[i])
        #     choose(_nums, r - 1, buffer[:])
        #     buffer.pop()
        
        # Use product
        from itertools import product
        results.extend(list(product(nums, repeat=m)))
        
    choose(nums, m, [])
    for rst in results:
        print(*rst, sep=" ")

if __name__=="__main__":
    N, M = map(int, input().split())
    solution(N, M)
