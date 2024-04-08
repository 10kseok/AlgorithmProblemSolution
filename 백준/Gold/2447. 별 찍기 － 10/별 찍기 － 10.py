import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def solution():
    N = int(input())
    # result = [[' '] * N for _ in range(N)]
    # def make_star(row, col, N):
    #     if N == 1:
    #         result[row][col] = '*'
    #         return
    #     sector = N // 3
        
    #     make_star(row, col, sector); make_star(row, col + sector, sector); make_star(row, col + sector * 2, sector)
    #     make_star(row + sector, col, sector); make_star(row + sector, col + sector * 2, sector)
    #     make_star(row + sector * 2, col, sector); make_star(row + sector * 2, col + sector, sector); make_star(row + sector * 2, col + sector * 2, sector)
    # make_star(0, 0, N)
    
    # print('\n'.join([''.join(result[i]) for i in range(N)]))
    
    
    def makeStars(n):
        if n == 3:
            star_list = ['***', '* *', '***']
            return star_list
        sector = makeStars(n//3)
        upper_and_lower = [x * 3 for x in sector]
        new_star_list = upper_and_lower + [x + ' ' * (n // 3) + x for x in sector] + upper_and_lower
        return new_star_list

    print('\n'.join(makeStars(N)))
if __name__=="__main__":
    solution() 

