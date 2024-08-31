class Solution {
    int solution(int[][] land) {
        int answer = 0;

        for (int row = 1; row < land.length; row++) {
            for (int col = 0; col < 4; col++) {
                int score = land[row][col];
                for (int i = 0; i < 4; i++) {
                    if (col == i)
                        continue;
                    score = Math.max(land[row][col] + land[row - 1][i], score);
                }
                land[row][col] = score;
            }
        }
        for (int i = 0; i < 4; i++) {
            answer = Math.max(answer, land[land.length - 1][i]);
        }
        return answer;
    }
}