import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Deque;
import java.util.LinkedList;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        String brackets = reader.readLine();

        writer.write(calculateBracketValue(brackets));
        reader.close();
        writer.close();
    }

    private static String calculateBracketValue(String brackets) {
        int result = 0;
        Deque<Character> stack = new LinkedList<>();
        int tempResult = 1;
        for (int i = 0; i < brackets.length(); i++) {
            Character curChar = brackets.charAt(i);
            switch (curChar) {
                case '(':
                    stack.addLast(curChar);
                    tempResult = tempResult << 1; // x2
                    break;
                case '[':
                    stack.addLast(curChar);
                    tempResult = (tempResult << 1) + tempResult; // x3
                    break;
                case ']':
                    if (stack.isEmpty() || stack.peekLast() != '[') {
                        result = 0;
                        return String.valueOf(result);
                    }
                    if (brackets.charAt(i - 1) == '[') result += tempResult;
                    stack.pollLast();
                    tempResult /= 3;
                    break;
                case ')':
                    if (stack.isEmpty() || stack.peekLast() != '(') {
                        result = 0;
                        return String.valueOf(result);
                    }
                    if (brackets.charAt(i - 1) == '(') result += tempResult;
                    stack.pollLast();
                    tempResult /= 2;
                    break;
                default:
                    break;
            }
        }
        if (!stack.isEmpty()) return "0";
        return String.valueOf(result);
    }
}