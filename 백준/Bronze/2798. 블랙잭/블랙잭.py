import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))
    
    global max_value
    max_value = 0
    def max_of_nCr(n, r, i, choices):
        global max_value
        if len(choices) == r:
            total = sum(choices)
            if max_value < total <= M:
                max_value = total
            return

        for idx in range(i, n):
            choices.append(cards[idx])
            max_of_nCr(n, r, idx + 1, choices)
            choices.pop()
    
    max_of_nCr(N, 3, 0, [])
    print(max_value)

if __name__=="__main__":
    solution()