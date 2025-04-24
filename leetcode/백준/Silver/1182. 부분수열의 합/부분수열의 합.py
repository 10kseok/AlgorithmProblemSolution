N, S = map(int, input().split())
nums = sorted(list(map(int, input().split())))
count = 0

# nCr로 모든 r을 1부터 N까지해서 모든 경우의수를 구함
# -> 시간 초과
# nCr로 r이 1부터 N까지 되면서 겹치는 항목들이 많았음
# 그래서 아예 처음부터 경우의 수가 n개에 도달할 때까지 경로를 모두 저장하려고함.
# def find_all_cases(element, r):
#     def generate_comb(i, cases, total):
#         global count
#         if len(cases) == r:
#             return
        
#         if total == S and len(cases) > 0:
#             count += 1
        
#         for j in range(i, len(element)):
#             cases.append(element[j])
#             generate_comb(j + 1, cases[:], total + element[j])
#             cases.pop()
#     generate_comb(0, [], 0)
    
# find_all_cases(nums, N)

def partial_sequence(idx, total):
    if N == idx:
        if S == total:
            return 1
        else:
            return 0
    return partial_sequence(idx + 1, total) \
        + partial_sequence(idx + 1, total + nums[idx])
count = partial_sequence(0, 0)
if S == 0: count -= 1
print(count)




