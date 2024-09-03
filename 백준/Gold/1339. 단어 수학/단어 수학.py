from sys import stdin

input = stdin.readline
        
def solution(n):
    alphabet_nums = [input().rstrip() for _ in range(n)]
    alphabet_to_value = {}
    
    for alphabet_num in alphabet_nums:
        digit = 1
        for i in range(len(alphabet_num) - 1, -1, -1):
            alphabet_to_value[alphabet_num[i]] = alphabet_to_value.get(alphabet_num[i], 0) + digit
            digit *= 10
    sorted_alphabets = sorted(alphabet_to_value.items(), key=lambda x:x[1], reverse=True)
    
    value = 9
    for alphabet, _ in sorted_alphabets:
        alphabet_to_value[alphabet] = value
        value -= 1
    
    total = 0
    for alphabet_num in alphabet_nums:
        for i in range(len(alphabet_num)):
            total += alphabet_to_value[alphabet_num[i]] * 10 ** (len(alphabet_num) - 1 - i)
    print(total)
    
if __name__=="__main__":
    n = int(input())
    solution(n)