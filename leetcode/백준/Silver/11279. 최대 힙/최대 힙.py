import sys
from heapq import heappush, heappop

n = int(input())
cmds = [int(sys.stdin.readline()) for _ in range(n)]

def heap(cmds):
    heap = []
    
    def push(x):
        heappush(heap, (-x, x))
    def pop():
        if len(heap) == 0: return 0
        return heappop(heap)[1]
    
    output = []
    for cmd in cmds:
        if cmd == 0:
            output.append(pop())
        elif cmd > 0:
            push(cmd)
    
    return map(str, output)

print('\n'.join(heap(cmds)))
