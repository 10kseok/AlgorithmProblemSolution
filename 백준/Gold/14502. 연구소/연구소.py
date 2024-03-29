import sys
input = sys.stdin.readline

DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동 서 남 북
def combinations(blanks, r):
    result = []
    
    def generate_comb(buf, start, k):
        if k == 0:
            result.append(buf[:])
            return
        for i in range(start, len(blanks)):
            buf.append(blanks[i])
            generate_comb(buf, i + 1, k - 1)
            buf.pop()
    generate_comb([], 0, r)
    return result

def spread_virus_by_dfs(lab_map, i, j):
    if lab_map[i][j] == 1:
        return
    lab_map[i][j] = 2
    for di, dj in DIRECTION:
        next_i, next_j = i + di, j + dj
        if next_i < 0 or next_i >= N or next_j < 0 or next_j >= M or lab_map[next_i][next_j] == 2:
            continue
        spread_virus_by_dfs(lab_map, next_i, next_j)
        
def spread_virus(lab_map):
    virus = []
    for i in range(N):
        for j in range(M):
            if lab_map[i][j] == 2:
                virus.append((i, j))
                
    for i, j in virus:            
        spread_virus_by_dfs(lab_map, i, j)
        
def retrieve_safe_area(lab_map):
    return len([0 for i in range(N) for j in range(M) if lab_map[i][j] == 0])
        
def solution():
    global N, M
    N, M = map(int, input().split())
    lab_map = [list(map(int, input().split())) for _ in range(N)]
    blanks = [(i, j) for i in range(N) for j in range(M) if lab_map[i][j] == 0]
    comb_blanks = combinations(blanks, 3)
    
    max_safe_area = 0
    for c1, c2, c3 in comb_blanks:
        copied_lab = [lab[:] for lab in lab_map]
        copied_lab[c1[0]][c1[1]], copied_lab[c2[0]][c2[1]], copied_lab[c3[0]][c3[1]] = 1, 1, 1
        spread_virus(copied_lab)
        safe_area = retrieve_safe_area(copied_lab)
        if safe_area > max_safe_area:
            max_safe_area = safe_area

    print(max_safe_area)
if __name__=="__main__":
    solution() 

