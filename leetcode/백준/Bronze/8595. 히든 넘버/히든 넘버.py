import sys
input = sys.stdin.readline

def solution():
    _ = input()
    word = input().rstrip()
    # 숫자가 나오면 문자가 나올 때까지 문자열을 더한다.
    # - 숫자는 ord를 통해 48 <=  <= 57임을 비교한다.
    # 문자면 아무 처리 없이 다음 문자로 넘어간다
    total = 0
    cur, last = 0, len(word)
    while cur < last:
        if (ord(word[cur]) < 48 or 57 < ord(word[cur])):
            cur += 1
            continue   
        num = word[cur]
        while True:
            next_char = cur + 1
            if next_char >= last or ord(word[next_char]) < 48 or 57 < ord(word[next_char]):
                cur += 1
                break
            num += word[next_char]
            cur += 1
        total += int(num)
        
    print(total)
    
if __name__=="__main__":
    solution() 

