n = int(input())
tops = list(map(int, input().split()))
answer = [0] * n

class Stack():
    def __init__(self) -> None:
        self.buffer = []
    
    def peek(self) -> tuple:
        return self.buffer[-1]
    
    def is_empty(self) -> bool:
        return len(self.buffer) == 0
    
    def push(self, value) -> None:
        self.buffer.append(value)

    def pop(self) -> tuple:
        return self.buffer.pop()

stack = Stack()
stack.push((1, tops[0]))

for i in range(1, n):
    while not stack.is_empty():
        if stack.peek()[1] > tops[i]:
            high_top_idx = stack.peek()[0]
            answer[i] = high_top_idx
            break
        else:
            stack.pop()
    stack.push((i + 1, tops[i]))

print(*answer)