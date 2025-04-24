from sys import stdin

input = stdin.readline
        
def solution(n):
    seq = [int(input()) for _ in range(n)]
    # stack, buffer, idx = [], [], 0
    # 전제조건: 수열은 1 ~ n의 수로 이루어져 있다.
    # stack에 1부터 n까지 push
    # buffer에 push, pop 연산 저장
    # stack에 있는 수열을 만들 수 있는지 확인
    # for i in range(1, n + 1):
    #     stack.append(i)
    #     buffer.append('+')
    #     while stack and stack[-1] == seq[idx]:
    #         stack.pop()
    #         buffer.append('-')
    #         idx += 1
    # print('\n'.join(buffer) if not stack else 'NO')
    
    # No Use index
    stack, buffer, num = [], [], 1
    
    for n in seq:
        while num <= n:
            stack.append(num)
            buffer.append('+')
            num += 1
        if stack.pop() != n:
            print('NO')
            return  
        buffer.append('-')
    print('\n'.join(buffer))
    
if __name__=="__main__":
    N = int(input())
    solution(N)
