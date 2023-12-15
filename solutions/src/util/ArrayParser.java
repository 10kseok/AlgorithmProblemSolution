package util;

import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

/**
 * Java로 알고리즘 문제 풀이 시
 * IDE에서 코드를 실행시키려면 입력값을 알맞은 객체로 파싱이 필요하다.
 * (주로 입력값이 배열일 때 파싱이 필요하다.)
 * 따라서, 입력값을 간편하게 파싱하기 위해 작성된 클래스이다.
 *
 * @author koesnam (추만석)
 * @since 2023.12.07
 */
public final class ArrayParser {
    public static int[][] parse(String array) {
        Deque<Chunk> bracketStack = new LinkedList<>();
        List<int[]> result = new LinkedList<>();
        String finedArray = array.replaceAll("\\s", "");
        char[] chars = finedArray.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            switch (chars[i]) {
                case '[':
                    bracketStack.add(new Chunk(chars[i], i));
                    break;
                case ']':
                    Chunk openBracket = bracketStack.pollLast();
                    // 제일 바깥 괄호인 경우
                    if (bracketStack.isEmpty()) {
                        continue;
                    }
                    if (openBracket == null || openBracket.content != '[') {
                        throw new RuntimeException("잘못된 입력 형태입니다. (열린 괄호가 존재하지 않아요!)");
                    }
                    int startIdx = openBracket.index + 1;
                    int[] parsedArray = Arrays.stream(finedArray.substring(startIdx, i).split(","))
                            .mapToInt(Integer::parseInt)
                            .toArray();
                    result.add(parsedArray);
                    break;
            }
        }
        return result.toArray(new int[0][]);
    }

    public static String[][] parse(String array, String dummy) {
        Deque<Chunk> bracketStack = new LinkedList<>();
        List<String[]> result = new LinkedList<>();
        String finedArray = array.replaceAll("[\\s\"]", "");
        char[] chars = finedArray.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            switch (chars[i]) {
                case '[':
                    bracketStack.add(new Chunk(chars[i], i));
                    break;
                case ']':
                    Chunk openBracket = bracketStack.pollLast();
                    // 제일 바깥 괄호인 경우
                    if (bracketStack.isEmpty()) {
                        continue;
                    }
                    if (openBracket == null || openBracket.content != '[') {
                        throw new RuntimeException("잘못된 입력 형태입니다. (열린 괄호가 존재하지 않아요!)");
                    }
                    int startIdx = openBracket.index + 1;
                    String[] parsedArray = finedArray.substring(startIdx, i).split(",");
                    result.add(parsedArray);
                    break;
            }
        }
        return result.toArray(new String[0][]);
    }

    private static class Chunk {
        private final char content;
        private final int index;

        public Chunk(char content, int index) {
            this.content = content;
            this.index = index;
        }
    }
}

class Test {
    enum Result {
        FAIL, SUCCESS
    }
    public static void main(String[] args) {
        ArrayParser parser = new ArrayParser();
        int[][] expect = new int[][]{
                {1, 2, 3},
                {1}};
        int[][] actual = parser.parse("[[1,2,3], [1]]");

        assert actual.length == expect.length : Result.FAIL;
        assert actual[0].length == expect[0].length : Result.FAIL;
        for (int i = 0; i < expect.length; i++) {
            for (int j = 0; j < expect[i].length; j++) {
                assert actual[i][j] == expect[i][j] : Result.FAIL;
            }
        }
        System.out.println(Result.SUCCESS);
    }
}