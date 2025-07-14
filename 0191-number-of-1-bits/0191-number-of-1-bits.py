class Solution:
    def hammingWeight(self, n: int) -> int:
        # 십진수 정수를 이진수로 바꿨을 때 1의 갯수를 구하라

        # 제약 조건
        # 1. 십진수 정수의 범위는 1 ~ 2^31 - 1
        # 2. 전달받는 파라미터는 십진수 형태의 정수 타입
        # 3. 이진수로 표현됐을 때의 1의 갯수

        # 문제
        # 1. 십진수를 이진수로 바꿨을 때 1의 갯수 구하는 것인데 다양한 형태의 풀이법이 있음
        # 2. bin를 활용해서 이진수 문자열로 바꾸고 진짜 숫자 카운트 방식
        # 3. 근데 이 방식을 요구하는 것 같진 않음
        # 4. int 타입에 이미 bit_count 메서드가 있어 이걸 활용해도 풀이 가능
        # 5. https://en.wikipedia.org/wiki/Hamming_weight를 참고하여 비트 연산자를 이용하여 푸는 방법 참고
        
        # 풀이 1
        # 1. 정수 타입에서 제공하는 해밍 웨이트 지원 메서드 사용
        return n.bit_count()

        # 풀이 2
        # 1. 비트 연산자를 이용한 방법
        # count = 0
        # while count < n:
        #     n &= n - 1
        #     count += 1
        # return count 