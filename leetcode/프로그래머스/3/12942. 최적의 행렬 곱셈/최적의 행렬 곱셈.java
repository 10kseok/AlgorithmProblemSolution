import java.util.*;

class Solution {
    public int solution(int[][] matrix_sizes) {
        int answer = 0;
        int n = matrix_sizes.length;
        
        int[] elems = new int[n + 1];
        elems[0] = matrix_sizes[0][0];
        for (int i = 1; i < n + 1; i++)
            elems[i] = matrix_sizes[i - 1][1];
        
        int[][] dp = new int[n + 1][n + 1];
        for (int i = 0; i < n + 1; i++)
            dp[i][i] = 0;
        
        for (int k = 1; k < n; k++) {
            for (int i = 1; i <= n - k; i++) {
                dp[i][i + k] = getMinimum(dp, elems, i, i + k);
            }    
        }                               
        return dp[1][n];
    }
    
    private static int getMinimum(int[][] dp, int[] elems, int i, int j) {
        int minValue = Integer.MAX_VALUE;
        for (int k = i; k < j; k++)
            minValue = Math.min(minValue, dp[i][k] + dp[k + 1][j] + elems[i - 1] * elems[k] * elems[j]);
        return minValue;
    }
}