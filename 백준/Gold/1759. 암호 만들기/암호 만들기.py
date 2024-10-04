from sys import stdin

input = stdin.readline

def solution(l, c):
    possible_characters = list(set(input().split()))
    possible_characters.sort(); c = len(possible_characters)
    vowels = set('aeiou')
    def find_password(chars: list, buffer: str, vowel: int, consonant: int):
        if len(buffer) == l and vowel >= 1 and consonant >= 2:
            answers.append(buffer)
            return
        for i in range(len(chars)):
            is_vowel = chars[i] in vowels
            find_password(chars[i + 1:], buffer + chars[i], vowel + int(is_vowel), consonant + int(not is_vowel))
    
    answers = []
    for i in range(c - l + 1):
        is_vowel = possible_characters[i] in vowels
        find_password(possible_characters[i + 1:], possible_characters[i], int(is_vowel), int(not is_vowel))
    
    print('\n'.join(answers))
if __name__=="__main__":
    L, C = map(int, input().split())
    solution(L, C)