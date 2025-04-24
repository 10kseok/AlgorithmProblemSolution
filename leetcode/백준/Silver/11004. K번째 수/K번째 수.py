def solve():
    n, k = map(int, input().split())
    arr = map(int, input().split())
    print(sorted(arr)[k - 1])
    
if __name__ == "__main__":
    solve()