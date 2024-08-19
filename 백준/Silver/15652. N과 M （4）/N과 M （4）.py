from sys import stdin

input = stdin.readline
        
def solution(n, m):
    nums = [i for i in range(1, n + 1)]
    results = []
    
    def choose(start, r, buffer):
        if r == 0:
            results.append(buffer)
            return
        
        for i in range(start, len(nums)):
            buffer.append(nums[i])
            choose(i, r - 1, buffer[:])
            buffer.pop()
        
    choose(0, m, [])
    
    # for rst in results:
    #     print(*rst, sep=" ")
    # For a lot of outputs
    print("\n".join(" ".join(map(str, result)) for result in results))

if __name__=="__main__":
    N, M = map(int, input().split())
    solution(N, M)
