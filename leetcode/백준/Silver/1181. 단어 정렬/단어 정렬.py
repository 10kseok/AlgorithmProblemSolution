import sys
n = int(input())
input_buffer = list(set([sys.stdin.readline() for _ in range(n)]))
input_buffer.sort(key=lambda x:(len(x), x))
sys.stdout.write(''.join(map(str, input_buffer)))
