n = int(input())
numbers = list(map(int, input().split()))

# for num in numbers:
#     if num == 1:
#         n -= 1

#     for j in range(2, num):
#         if num % j == 0:
#             n -= 1
#             break
# print(n)

# import math
# 1차 개선
# 약수의 구조는 대칭이다. 그러니 입력받은 수의 제곱근까지만 소수를 판별한다.
# for num in numbers:
#     if num == 1:
#         n -= 1
#     sqrt_num = int(math.sqrt(num)) + 1
#     for j in range(2, sqrt_num):
#         if num % j == 0:
#             n -= 1
#             break
# print(n)

# 에라토스테네스의 체
# 2부터 약수들을 지워낸다.
# 1 ~ n까지 소수, 즉 많은 양의 소수를 구하려할 때 용이하다.
max_value = max(numbers)
prime_table = [True for _ in range(max_value + 1)]
prime_table[0], prime_table[1] = False, False

for i in range(2, max_value + 1):
    if not prime_table[i]: continue
    for multiple in range(i, max_value + 1, i):
        if not prime_table[multiple]: continue
        if i != multiple: prime_table[multiple] = False

print(sum([prime_table[num] for num in numbers]))