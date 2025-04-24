from sys import stdin

input = stdin.readline
        
def solution(n, m):
    nums = list(map(str, sorted(list(map(int, input().split())))))
    results = []
    
    def choose(nums, r, buffer):
        # use Recursive
        if r == 0:
            results.append(buffer)
            return
        
        for i in range(len(nums)): 
            # buffer.append(nums[i])
            choose(nums[:i] + nums[i + 1:], r - 1, buffer + [nums[i]])
            # buffer.pop()
        
        # use while-loop
        # stack = [(nums, r, buffer)]
        # while stack:
        #     _nums, cnt, _buffer = stack.pop()
            
        #     if cnt == 0:
        #         results.append(_buffer)
        #         continue
            
        #     for i in range(len(_nums) - 1, -1, -1):
        #         stack.append((_nums[:i] + _nums[i + 1:], cnt - 1, _buffer[:] + [nums[i]]))

    choose(nums, m, [])
    
    # for rst in results:
    #     print(*rst, sep=" ")
    # For a lot of outputs
    print("\n".join(" ".join(result) for result in results))

if __name__=="__main__":
    N, M = map(int, input().split())
    solution(N, M)
