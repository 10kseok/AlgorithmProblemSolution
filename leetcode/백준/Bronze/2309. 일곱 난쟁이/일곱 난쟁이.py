dwalfs = sorted([int(input()) for _ in range(9)])

def generate_combinations(elements, r):
    """
    주어진 리스트에서 길이가 r인 모든 조합을 생성하는 함수

    Parameters:
    - elements: 리스트 (조합을 생성할 대상)
    - r: 조합의 길이

    Returns:
    - 모든 조합을 담은 리스트
    """
    def backtrack(start, path):
        if len(result) == 1: return
        if len(path) == r:
            if sum(path) == 100:
                result.append(path)
            return
        for i in range(start, len(elements)):
            path.append(elements[i])
            backtrack(i + 1, path[:])
            path.pop()

    result = []
    backtrack(0, [])
    return result
    return result

print('\n'.join(map(str, *generate_combinations(dwalfs, 7))))