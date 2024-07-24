from sys import stdin

input = stdin.readline

def solution(N, students):    
    # Use counter
    # counter = [0] * 40_001
    # answer = 0

    # for i in range(N):
    #     answer += counter[20_000 - students[i]]
    #     for j in range(i):
    #         counter[20_000 + students[i] + students[j]] += 1   
    # print(answer)
    
    # Use Two-pointer
    # students.sort()
    # answer = 0
    # for i in range(N):
    #     if students[i] > 0:
    #         break
    #     lower, upper = i + 1, N - 1
    #     while lower < upper:
    #         total = students[lower] + students[upper]
    #         if total < -students[i]:
    #             lower += 1
    #         elif total > -students[i]:
    #             upper -= 1
    #         else:
    #             if students[lower] == students[upper]:
    #                 # nCr => nC2
    #                 n = upper - lower
    #                 answer += (n + 1) * n // 2
    #                 break
    #             else:
    #                 # 중복 lower * 중복 upper
    #                 dup_lower, dup_upper = 1, 1
    #                 while students[lower] == students[lower + 1]:
    #                     lower += 1
    #                     dup_lower += 1
    #                 while students[upper] == students[upper - 1]:
    #                     upper -= 1
    #                     dup_upper += 1
    #                 answer += dup_lower * dup_upper
    #                 upper -= 1 # 다른 조합도 있는지 확인하기 위해 (lower와 upper가 연속적인 수가 아닐 때 발생)
    # print(answer)
    
    # Use divided counter
    answer = 0 
    positive = [0] * 10001
    negative = [0] * 10001
    for student in students: 
        if student < 0:
            negative[abs(student)] += 1
        else:
            positive[student] += 1
            
    def pick_two(cur, container):
        local_total = 0
        for i in range(cur // 2 + 1):
            if i != cur - i:
                local_total += container[i] * container[cur - i]
        
        if cur % 2 == 0:
            middle_couple = container[cur // 2]
            if middle_couple >= 2:
                local_total += middle_couple * (middle_couple - 1) // 2

        return local_total
    
    for i in range(1, 10001):
        if positive[i]:
            answer += pick_two(i, negative) * positive[i]
        if negative[i]:
            answer += pick_two(i, positive) * negative[i]

    if positive[0] >= 3:
        zero_val = positive[0]
        answer += zero_val * (zero_val - 1) * (zero_val - 2) // 6
    print(answer)
    
if __name__=="__main__":
    N = int(input())
    students = list(map(int, input().split()))
    solution(N, students)
