def solution(n, s):
    if n > s:
        return [-1]
    # 3, 9
    # {3, 3, 3} = 27, {4, 4, 1} = 16, {3, 4, 2} = 24
    # {..., Sn-2 // n - 2, Sn-1 // n - 1, S // n}
    # 2, 9
    # 9 - 0 // n = 3, 9 - 3 // n = 3, 6 - 3 // n = 3 
    # 3, 3, 3
    answer = [0] * (n + 1)
    buffer = [s] * (n + 1)
    for i in range(n - 1, -1, -1):
        answer[i] = buffer[i + 1] // n
        buffer[i] = buffer[i + 1] - answer[i]
        n -= 1
    return sorted(answer[:-1])