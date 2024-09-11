import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        boolean[][] matchingBoard = new boolean[n + 1][n + 1];
        
        for (int[] result : results) {
            int winner = result[0], loser = result[1];
            matchingBoard[winner][loser] = true;
        }
        
        for (int i = 1; i < n + 1; i++)
            matchingBoard[i][i] = true;
        
        for (int stepover = 1; stepover < n + 1; stepover++) {
            for (int i = 1; i < n + 1; i++) {
                for (int j = 1; j < n + 1; j++) {
                    if (matchingBoard[i][stepover] && matchingBoard[stepover][j])
                        matchingBoard[i][j] = true;
                }
            }
        }
        
        int answer = 0;
        for (int i = 1; i < n + 1; i++) {
            boolean[] player = matchingBoard[i];
            int totalResult = 0;
            for (int j = 1; j < n + 1; j++) {
                if (matchingBoard[i][j] || matchingBoard[j][i])
                    totalResult++;
            }
            if (totalResult == n)
                answer++;
        }
        
        return answer;
    }
}