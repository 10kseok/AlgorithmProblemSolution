import java.util.*;

class Solution {
    private static String[] board;
    private static int[][] countBoard;
    private static int MAX_VALUE = 100 * 100 + 1;
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
            Arrays.fill(row, MAX_VALUE);
        }
        
        int goalRow = 0, goalCol = 0;
        int startRow = 0, startCol = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length(); j++) {
                if (board[i].charAt(j) == 'R') {
                    countBoard[i][j] = 0;
                    // for (int[] direction: directions) {
                    //     int nextRow = i + direction[0], nextCol = j + direction[1];
                    //     if (isAvailable(nextRow, nextCol))
                    //         dfs(direction, i, j, 0);
                    // }
                    startRow = i;
                    startCol = j;
                }
                if (board[i].charAt(j) == 'G') {
                    goalRow = i;
                    goalCol = j;
                }
            }
        }
        // return countBoard[goalRow][goalCol] != MAX_VALUE ? countBoard[goalRow][goalCol] : -1;
        return bfs(startRow, startCol, goalRow, goalCol);
    }
    
    // private static void dfs(int[] direction, int row, int col, int count) {
    //     int nextRow = row + direction[0], nextCol = col + direction[1];
    //     if (!isAvailable(nextRow, nextCol)) {
    //         if (countBoard[row][col] <= count + 1)
    //             return;
    //         countBoard[row][col] = count + 1;
    //         for (int[] d: directions) {
    //             if (d[0] == -direction[0] && d[1] == -direction[1])
    //                 continue;
    //             nextRow = row + d[0]; nextCol = col + d[1];
    //             if (isAvailable(nextRow, nextCol)) {
    //                 dfs(d, nextRow, nextCol, count + 1);
    //             }
    //         }   
    //     } else 
    //         dfs(direction, nextRow, nextCol, count);
    // }
    
    private static int bfs(int startRow, int startCol, int goalRow, int goalCol) {
        // Position {row, col, count}
        Queue<int[]> queue = new LinkedList();
        queue.offer(new int[] { startRow, startCol, 0 });
        while (!queue.isEmpty()) {
            int[] position = queue.poll();
            int row = position[0], col = position[1], count = position[2];
            if (row == goalRow && col == goalCol)
                return count;
            
            for (int[] d: directions) {
                int nextRow = row + d[0], nextCol = col + d[1];
                if (!isAvailable(nextRow, nextCol))
                    continue;
                
                while (isAvailable(nextRow, nextCol)) {
                    nextRow += d[0];
                    nextCol += d[1];
                }
                nextRow -= d[0];
                nextCol -= d[1];
                if (countBoard[nextRow][nextCol] > count + 1) {
                    countBoard[nextRow][nextCol] = count + 1;
                    queue.offer(new int[] { nextRow, nextCol, count + 1 });    
                }
            }  
        }
        return -1;
    }
    
    private static boolean isAvailable(int row, int col) {
        if (0 <= row && row < board.length && 0 <= col && col < board[0].length() && board[row].charAt(col) != 'D')
            return true;
        return false;
    }
}