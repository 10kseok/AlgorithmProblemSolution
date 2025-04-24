import sys

# 입력 횟수를 입력받는다.
# 입력을 받은 후 반복해야하는 횟수와 단어를 설정한다.
# 단어를 순회하면서 반복해야하는 횟수만큼 문자열을 더해간다.
# 출력한다.
n = int(input())

for _ in range(n):
    cnt, word = sys.stdin.readline().split()

    output = ''
    for char in word:
        output += int(cnt) * char
    print(output)

# string concatenate가 안 되는 언어일 경우
# for _ in range(n):
#     cnt, word = sys.stdin.readline().split()

#     output = []
#     for char in word:
#         for _ in range(int(cnt)):
#             output.append(char)
#     print(''.join(output))