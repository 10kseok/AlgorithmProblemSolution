from sys import stdin

input = stdin.readline

def solution(N, students):    
    counter = [0] * 40_001
    answer = 0
    students.sort()
    for i in range(N):
        answer += counter[20_000 - students[i]]
        for j in range(i):
            counter[20_000 + students[i] + students[j]] += 1
            
    print(answer)

if __name__=="__main__":
    N = int(input())
    students = list(map(int, input().split()))
    solution(N, students)