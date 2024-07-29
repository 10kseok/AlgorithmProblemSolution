from sys import stdin

input = stdin.readline

def solution(n):
    num_table = [tuple(map(int, input().split())) for _ in range(n)]
    min_max = list(map(lambda x: [x, x], num_table[0]))
    MIN, MAX = 0, 1
    for i in range(1, n):
        min_a = min(min_max[0][MIN], min_max[1][MIN]) + num_table[i][0]
        max_a = max(min_max[0][MAX], min_max[1][MAX]) + num_table[i][0]
        
        min_b = min(min_max[0][MIN], min_max[1][MIN], min_max[2][MIN]) + num_table[i][1]
        max_b = max(min_max[0][MAX], min_max[1][MAX], min_max[2][MAX]) + num_table[i][1]
        
        min_c = min(min_max[1][MIN], min_max[2][MIN]) + num_table[i][2]
        max_c = max(min_max[1][MAX], min_max[2][MAX]) + num_table[i][2]
        
        min_max[0][MIN], min_max[0][MAX] = min_a, max_a
        min_max[1][MIN], min_max[1][MAX] = min_b, max_b
        min_max[2][MIN], min_max[2][MAX] = min_c, max_c
    
    print(max(map(lambda x: x[1], min_max)), min(map(lambda x: x[0], min_max)))
if __name__=="__main__":
    N = int(input())
    solution(N)