import sys
from collections import deque

n = int(input())
cmds = [sys.stdin.readline() for _ in range(n)]

def queue(cmds):
    buffer = deque()
    output = []
    def size():
        return len(buffer)
    def push(x):
        buffer.append(x)
    def pop():
        if size() == 0:
            return -1
        return buffer.popleft()
    def empty():
        return size() == 0
    def top():
        if empty(): return -1
        return buffer[-1]
    def front():
        if empty(): return -1
        return buffer[0]
    def back():
        if empty(): return -1
        return buffer[-1]
    
    for cmd in cmds:
        if cmd.startswith('push'):
            push(cmd.split()[1])
            continue
        
        match cmd.rstrip():
            case "pop":
                output.append(f'{pop()}')
            case "size":
                output.append(f'{size()}')
            case "empty":
                output.append(f'{int(empty())}')
            case "front":
                output.append(f'{front()}')
            case "back":
                output.append(f'{back()}')

    return output

print('\n'.join(queue(cmds)))