import sys
input = sys.stdin.readline

def solution():
    INTERVIEW = 1

    T = int(input())
    result = []
    for _ in range(T):
        N = int(input())
        new_recruits = []

        for _ in range(N):
            paper, interview = map(int, input().split())
            new_recruits.append((paper, interview))
        new_recruits.sort()

        count = 1
        prev_recruit = new_recruits[0]
        for recruit in new_recruits[1:]:
            if prev_recruit[INTERVIEW] > recruit[INTERVIEW]:
                prev_recruit = recruit
                count += 1

        result.append(count)
    print(*result, sep="\n")
    
if __name__=="__main__":
    solution()