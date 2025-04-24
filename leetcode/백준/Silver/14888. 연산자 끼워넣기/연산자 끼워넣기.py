import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split())) # + - * /
    
    min_max_value = [1e9 + 1, -1e9 - 1]
    def operate(depth, result):
        if (depth == N):
            min_max_value[0] = min(min_max_value[0], result)
            min_max_value[1] = max(min_max_value[1], result)
        for i in range(4):
            if operators[i] == 0: continue
            operators[i] -= 1
            match i:
                case 0:
                    operate(depth + 1, result + numbers[depth])
                case 1:
                    operate(depth + 1, result - numbers[depth])
                case 2:
                    operate(depth + 1, result * numbers[depth])
                case 3:
                    operate(depth + 1, int(result / numbers[depth]))
            operators[i] += 1
            
    operate(1, numbers[0])
    print(*min_max_value[::-1], sep="\n")
                         
if __name__=="__main__":
    solution()
    