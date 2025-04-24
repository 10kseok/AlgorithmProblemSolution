def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = [0, 0, 0]
    one_answer_size, two_answer_size, three_answer_size = len(one), len(two), len(three)
    
    for i in range(len(answers)):
        ans = answers[i]
        if one[i % one_answer_size] == ans:
            answer[0] += 1
        if two[i % two_answer_size] == ans:
            answer[1] += 1
        if three[i % three_answer_size] == ans:
            answer[2] += 1
    best = max(answer)
    result = []
    for i in range(3):
        if answer[i] == best:
            result.append(i + 1)
    return result