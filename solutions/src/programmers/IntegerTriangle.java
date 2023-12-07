package programmers;

import java.util.Arrays;
import util.ArrayParser;

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/43105
 * 정수 삼각형
 *
 * 풀이 :
 * 동적 계획법 사용. DFS로 트리를 만들어 순회하려 했으나, 그렇게 되면 중복으로 순회하는 것이 높이가 높아질수록 많아지므로 동적 계획법을 사용했어야 했다.
 *
 * @author koesnam (추만석)
 * @since 2023.12.08
 */
public class IntegerTriangle {
    public int solution(int[][] triangle) {
//        for (int i = 1; i < triangle.length; i++) {
//            for (int j = 0; j < triangle[i].length; j++) {
//                if (j == 0) {
//                    triangle[i][j] += triangle[i - 1][j];
//                } else if (j == triangle[i].length - 1) {
//                    triangle[i][j] += triangle[i - 1][j -1];
//                } else {
//                    triangle[i][j] += Math.max(triangle[i - 1][j - 1], triangle[i - 1][j]);
//                }
//            }
//        }
        // 1차 개선
        // triangle[i].length - 1 (=한 계층의 마지막 인덱스)는 사실상 i 값이랑 동일하다.
        for (int i = 1; i < triangle.length; i++) {
            triangle[i][0] += triangle[i - 1][0]; // 젤 처음 값
            triangle[i][i] += triangle[i - 1][i - 1]; // 젤 마지막 값
            // 중간 값
            for (int j = 1; j < i; j++) {
                triangle[i][j] += Math.max(triangle[i - 1][j - 1], triangle[i - 1][j]);
            }
        }
        return Arrays.stream(triangle[triangle.length - 1])
                .max()
                .orElseThrow();
    }

    public static void main(String[] args) {
        IntegerTriangle actual = new IntegerTriangle();
        System.out.println(actual.solution(ArrayParser.parse("[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]")));
    }
}
