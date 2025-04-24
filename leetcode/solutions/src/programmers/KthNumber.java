package programmers;

import java.util.Arrays;

/**
 * KthNumber
 */
public class KthNumber {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int i = 0; i < commands.length; i++) {
            int[] cmd = commands[i];
            // index 기준으로 할당
            int start = cmd[0] - 1;
            int end = cmd[1] - 1;
            int target = cmd[2] - 1;

            int[] slicedArray = Arrays.copyOfRange(array, start, end + 1);
            Arrays.sort(slicedArray);
            answer[i] = slicedArray[target];
        }
        return answer;
    }

    public static void main(String[] args) {
        KthNumber kthNumber = new KthNumber();
        Arrays.stream(kthNumber.solution(new int[] { 1, 5, 2, 6, 3, 7, 4 },
                new int[][] { { 2, 5, 3 }, { 4, 4, 1 }, { 1, 7, 3 } }))
                .forEach(System.out::println);
    }
}
