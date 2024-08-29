import java.util.*;

class Solution {
    private static String[] board;
    private static int[][] countBoard;
    
    private static int[][] directions = new int[][] {
        { 1,  0},
        {-1,  0},
        { 0,  1},
        { 0, -1}
    };
    
    public int solution(String[] board) {
        Solution.board = board;
        int answer = 0;
        countBoard = new int[board.length][board[0].length()];
        for (int[] row : countBoard) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        
        int goalRow = 0, goalCol = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length(); j++) {
                if (board[i].charAt(j) == 'R') {
                    countBoard[i][j] = 0;
                    for (int[] direction: directions) {
                        int nextRow = i + direction[0], nextCol = j + direction[1];
                        if (isAvailable(nextRow, nextCol))
                            dfs(direction, i, j, 0);
                    }
                }
                if (board[i].charAt(j) == 'G') {
                    goalRow = i;
                    goalCol = j;
                }
            }
        }
        
        for (int[] row : countBoard) {
            System.out.println(Arrays.toString(row));
        }
        
        return countBoard[goalRow][goalCol] != Integer.MAX_VALUE ? countBoard[goalRow][goalCol] : -1;
    }
    
    private static void dfs(int[] direction, int row, int col, int count) {
        int nextRow = row + direction[0], nextCol = col + direction[1];
        if (!isAvailable(nextRow, nextCol)) {
            if (countBoard[row][col] <= count + 1)
                return;
            countBoard[row][col] = count + 1;
            for (int[] d: directions) {
                if (d[0] == -direction[0] && d[1] == -direction[1])
                    continue;
                nextRow = row + d[0]; nextCol = col + d[1];
                if (isAvailable(nextRow, nextCol)) {
                    dfs(d, nextRow, nextCol, count + 1);
                }
            }   
        } else 
            dfs(direction, nextRow, nextCol, count);
    }
    
    private static boolean isAvailable(int row, int col) {
        if (0 <= row && row < board.length && 0 <= col && col < board[0].length() && board[row].charAt(col) != 'D')
            return true;
        return false;
    }
}