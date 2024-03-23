def solution(numbers):
    answer = 0
    visited = [False] * 7
    nums = set()
    
    def perm(numbers, num, depth):
        if depth > len(numbers):
            return
        
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                nums.add(int(f'{num}{numbers[i]}'))
                perm(numbers, f'{num}{numbers[i]}', depth + 1)
                visited[i] = False
    
    perm(numbers, "", 0)
    
    for n in nums:
        if n == 0 or n == 1:
            continue
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
        if is_prime:
            answer += 1
    return answer