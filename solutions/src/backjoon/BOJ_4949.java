package backjoon;

import java.io.*;
import java.util.*;

/*
    ** 스택 기본 문제 **
    카운터로 풀이시 반례 : Help( I[m being held prisoner in a fortune cookie factory)].
    --> 갯수는 맞게 되었으나 짝이 맞지 않음.

    괄호가 짝이 맞아야 한다. -> 닫는 괄호를 만나면 직전에 만난 여는 괄호가 같은 종류인지 확인해야함
    --> 여는 괄호시 Stack에 삽입, 닫는 괄호시 Stack에서 pop를 통해 같은 종류의 괄호인지 확인하고 결과 출력
 */

public class BOJ_4949 {
    public static void solution() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        HashMap<Character, Character> symmetryMap = new HashMap<>() {{
            put(')', '(');
            put(']', '[');
        }};

        String line;
        while (!((line = reader.readLine()).equals("."))) {
            ArrayDeque<Character> stack = new ArrayDeque<>();
            String result = "yes\n";
            for (char c : line.toCharArray()) {
                if (result.equals("no\n")) break;
                switch (c) {
                    case '(' : case '[':
                        stack.add(c);
                        break;

                    case ')' : case ']':
                        // *Tip: ArrayDeque의 removeLast는 비었을 시 오류 반환, pollLast는 null 반환
                        // 괄호가 짝이 맞는지 확인
                        result = (symmetryMap.get(c).equals(stack.pollLast())) ? "yes\n" : "no\n";
                        break;
                }
            }
            // 괄호가 짝에 맞게 있었다면 스택이 비워져있어야함 + 괄호가 아예 안 나오는 경우도 균형으로 인정
            if (!stack.isEmpty()) result = "no\n";
            writer.write(result);
        }

        reader.close();
        writer.close();
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BOJ_4949.solution();
    }
}

