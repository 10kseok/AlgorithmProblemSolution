class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 주어진 괄호 쌍의 갯수에서 만들 수 있는 괄호 구하기
        
        # 제약 조건
        # 1. 괄호 쌍의 갯수는 1~8개
        # 2. 올바른 괄호 쌍으로 만들어야함 ex_ n = 3 ')))(((' -> x

        # 문제
        # 1. 올바른지 괄호인지 판단은 구성해봐야 알 수 있다.
        # 2. 처음과 끝은 무조건 '('와 ')'로 고정
        # 3. 그러면 n이 8까지이므로 모든 경우는 최대 2*14개까지 생성 가능
        # 4. 생성된 괄호 중에서 올바른 괄호만 추출 필요

        # 풀이 (브루트포스)
        # 1. '('로 시작하여 (n-1) * 2개의 자리에 '(' or ')'로 구성하여 새로운 괄호 조합 생성
        # 2. 괄호 조합에서 스택을 활용하여 짝이 제대로 맞는지 확인
        # 3. 짝이 제대로된 괄호 조합만 추출해서 정답 배열에 추가

        # if n == 1:
        #     return ["()"]
        
        # parentheses: list[str] = []

        # def generate(buffer: str):
        #     if len(buffer) == n * 2:
        #         parentheses.append(buffer)
        #         return 
            
        #     for l in ('(', ')'):
        #         generate(buffer + l)

        # generate('(')
        
        # answer: list[str] = []
        # for prnths in parentheses:
        #     is_well_formed = True
        #     balance = 0
        #     for p in prnths:
        #         balance += 1 if p == '(' else -1
        #         if balance < 0 or balance > n:
        #             is_well_formed = False
        #     if balance == 0 and is_well_formed:
        #         answer.append(prnths)

        # 풀이 2
        # 1. 올바른 괄호는 왼쪽과 오른쪽의 갯수가 같으면서 둘의 합이 2n인 경우다.
        # 2. 왼쪽 괄호가 오른쪽보다 많으면 오른쪽 괄호를 추가한다.
        # 3. 오른쪽 괄호가 왼쪽보다 많으면 왼쪽 괄호를 추가한다.
        # 4. 올바른 괄호가 되면 종료한다.
        answer: list[str] = []
        def generate(left_count, right_count, buffer):
            print(buffer, left_count, right_count)
            if left_count == right_count and left_count + right_count == 2 * n:
                answer.append(buffer)
                return

            if left_count < n:
                generate(left_count + 1, right_count, buffer + '(')
            if right_count < left_count:
                generate(left_count, right_count + 1, buffer + ')')

        generate(0, 0, '')
        return answer