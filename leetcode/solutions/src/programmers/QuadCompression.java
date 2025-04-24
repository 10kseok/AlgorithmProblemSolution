package programmers;

/**
 * QuadCompression
 */
public class QuadCompression {
    static Counter counter = new Counter(2);

    public int[] solution(int[][] arr) {
        compress(arr, 0, 0, arr.length);
        return counter.getScores();
    }

    public static void compress(final int[][] arr, int startRowIdx, int startColIdx, int length) {
        int total = 0;
        for (int i = startRowIdx; i < startRowIdx + length; i++) {
            for (int j = startColIdx; j < startColIdx + length; j++) {
                total += arr[i][j];
            }
        }

        // 0 또는 1로만 구성되면 압축 성공 (1개만 있을 때도 포함)
        if (total == 0) {
            counter.increase(0, 1);
            return;
        }
        if (total == length * length) {
            counter.increase(1, 1);
            return;
        }

        // 압축 실패시 영역 나눔
        length /= 2;
        compress(arr, startRowIdx, startColIdx, length); // 2사분면
        compress(arr, startRowIdx, startColIdx + length, length); // 1사분면
        compress(arr, startRowIdx + length, startColIdx, length); // 3사분면
        compress(arr, startRowIdx + length, startColIdx + length, length); // 4사분면
    }

    static class Counter {
        private int[] scores;

        public Counter(int n) {
            this.scores = new int[n];
        }

        public void increase(int numKey, int amount) {
            scores[numKey] += amount;
        }

        public int[] getScores() {
            return scores;
        }
    }
}