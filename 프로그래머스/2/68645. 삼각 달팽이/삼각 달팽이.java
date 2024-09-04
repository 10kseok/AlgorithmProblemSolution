import java.util.*;

class Solution {
    public int[] solution(int n) {
        int verticesLength = (int) Math.ceil(n / 3.0);
        int[][] vertices = new int[verticesLength][2];
        int row = 0, col = 0;
        for (int i = 0; i < verticesLength; i++) {
            vertices[i] = new int[] {row, col};
            row += 2;
            col += 1;
        }
        
        int[][] triangle = new int[n][];
        for (int i = 0; i < n; i++)
            triangle[i] = new int[i + 1];
        triangle[0][0] = 1;
        
        for (int[] vertex : vertices) {
            row = vertex[0];
            col = vertex[1];
            if (row > 0 && col > 0) {
                triangle[row][col] = triangle[row - 1][col] + 1;
            }
            // 왼쪽
            while (row < n - 1 && triangle[row + 1][col] == 0) {
                triangle[row + 1][col] = triangle[row++][col] + 1;
            }
            // 밑바닥
            while (col < row && triangle[row][col + 1] == 0) {
                triangle[row][col + 1] = triangle[row][col++] + 1;
            }
            // 오른쪽
            while (0 < row && triangle[row - 1][col - 1] == 0) {
                triangle[row - 1][col - 1] = triangle[row--][col--] + 1;
            }
        }
        
        int index = 0;
        int[] answer = new int[n * (n + 1) / 2];
        for (int[] trng: triangle) {
            for (int num : trng)
                answer[index++] = num;    
        }
        
        return answer;
    }
}