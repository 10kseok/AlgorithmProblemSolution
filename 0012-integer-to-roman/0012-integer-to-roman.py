class Solution:
    def intToRoman(self, num: int) -> str:
        # 주어진 십진수를 특정 규칙을 통해 로마자로 변경해라

        # 제약 조건
        # 1. 주어진 숫자 범위 [1, 3999]
        # 2. 4와 9로 시작하지 않으면 뺄 수 있는 가장 큰 값의 심볼로 나타내라
        # 3. 뺀 값의 나머지도 로마자로 나타내야 한다
        # 4. 4와 9로 시작하면 근사치 중 가장 큰 값에서 뺀 형태로 나타내라
        # 5. Big endian으로 표현
        # 6. 4 또는 9 시작이면 Little endian
        # 7. 십진수 자리 기반으로 계산

        # 문제
        # 1. 각 자릿수별로 로마자로 변환해야한다 (십의 자리를 일의 자리로 나타내는 것 x)
        # 2. 4,9냐 아니냐에 따라 다른 변환 규칙이 적용된다.

        # 풀이
        # 1. 작은 숫자부터 탐색하여 규칙을 적용시켜나간다.
        # 2. 4면 해당 자리수의 1과 5 순서로 변환
        # 3. 9면 해당 자리수보다 현단계 1과 한단계 높은 자리수의 1로 변환
        # 3. 그게 아니면 해당 자릿수의 5와 1 순서로 그리디하게 변환

        SYMBOLS = [('I', 'V'), ('X', 'L'), ('C', 'D'), ('M', '')]
        ONE, FIVE = 0, 1
        num_for_iter = str(num)[::-1]
        n = len(num_for_iter)
        roman_numeral = ''
        for i in range(n):
            if num_for_iter[i] == '4':
                roman_numeral = SYMBOLS[i][ONE] + SYMBOLS[i][FIVE] + roman_numeral
            elif num_for_iter[i] == '9':
                roman_numeral = SYMBOLS[i][ONE] + SYMBOLS[i+1][ONE] + roman_numeral
            else:
                num = int(num_for_iter[i])
                five_count = int(num >= 5)
                one_count = num % 5
                roman_numeral = SYMBOLS[i][FIVE] * five_count + SYMBOLS[i][ONE] * one_count + roman_numeral

        return roman_numeral

        