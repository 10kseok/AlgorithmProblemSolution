import sys
input = sys.stdin.readline

def solution():
    expression = input().rstrip()
    
    stack = []
    answer = []
    for exp in expression:
        if exp == '(':
            stack.append(exp)
        elif exp == ')':
            while stack and stack[-1] != '(':
                answer.append(stack.pop())
            stack.pop()
        elif exp in '+-':
            while stack and stack[-1] != '(':
                answer.append(stack.pop())
            stack.append(exp)
        elif exp in '*/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer.append(stack.pop())
            stack.append(exp)
        else:
            answer.append(exp)
    while stack:
        answer.append(stack.pop())
        
    print(''.join(answer))
if __name__=="__main__":
    solution() 
