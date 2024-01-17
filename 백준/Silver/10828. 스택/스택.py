import sys

n = int(input())
cmds = [sys.stdin.readline() for _ in range(n)]

def stack(cmds):
    buffer = []
    output = []
    def size():
        return len(buffer)
    def pop():
        if size() == 0:
            return -1
        return buffer.pop()
    def empty():
        return size() == 0
    def top():
        if empty(): return -1
        return buffer[-1]

    for cmd in cmds:
        if cmd.startswith('push'):
            buffer.append(cmd.split()[1])
            continue
        
        match cmd.rstrip():
            case "pop":
                output.append(f'{pop()}')
            case "size":
                output.append(f'{size()}')
            case "empty":
                output.append(f'{int(empty())}')
            case "top":
                output.append(f'{top()}')

    return output


print('\n'.join(stack(cmds)))