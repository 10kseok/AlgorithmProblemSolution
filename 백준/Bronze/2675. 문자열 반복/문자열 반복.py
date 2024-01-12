import sys

n = int(input())

# string concatenate가 안 되는 언어일 경우
for _ in range(n):
    cnt, word = sys.stdin.readline().split()

    output = []
    for char in word:
        for _ in range(int(cnt)):
            output.append(char)
    print(''.join(output))