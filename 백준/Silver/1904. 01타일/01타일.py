N = int(input())

def cal_cases(n):
    tile_cases = {1 : 1, 2 : 2}

    if n not in tile_cases.keys():
        for i in range(3, N+1):
            tile_cases[i] = (tile_cases[i-1] + tile_cases[i-2]) % 15746

    return tile_cases[n]

print(cal_cases(N))