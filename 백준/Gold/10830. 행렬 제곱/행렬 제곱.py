import sys
input = sys.stdin.readline

def solution():
    N, B = map(int, input().split())
    base_matrix = [list(map(int, input().split())) for _ in range(N)]
    result_table = {}
    result_table['1'] = base_matrix
    
    def _product(matrixA, matrixB):
        temp = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                total = 0
                for k in range(N):
                    total += (matrixA[i][k] * matrixB[k][j])
                temp[i][j] = total % 1000
        return temp
    
    def product(base, power, result):
        if result_table.get(f"{power}", False) : return result_table[f"{power}"]
        if power % 2 == 0:
            result = _product(product(base, power // 2, result), product(base, power // 2, result))
            result_table[f"{power}"] = result
            return result
        else:
            result = _product(product(base, power - 1, result), product(base, 1, result))    
            result_table[f"{power}"] = result
            return result     
        
    result = product(base_matrix[:], B, base_matrix[:])
    
    for array in result:
        print(*map(lambda x: x % 1000, array))

if __name__=="__main__":
    solution()