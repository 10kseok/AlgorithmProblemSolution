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
    
    value_num, total = 9, 0
    for _, value in sorted_alphabets:
        total += value_num * value
        value_num -= 1
    print(total)
    
if __name__=="__main__":
    n = int(input())
    solution(n)