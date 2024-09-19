import java.util.*;

class Solution {
    private static int n;
    private static int height;
    private static int[][] land;
    
    private static int[] dr = new int[] {1, -1, 0, 0};
    private static int[] dc = new int[] {0, 0, 1, -1};
        
    public int solution(int[][] land, int height) {
        Solution.height = height;
        Solution.n = land.length;
        Solution.land = land;
        
        int answer = Integer.MAX_VALUE;
        answer = traverseForMinimum(0, 0);
        return answer;
    }
    
    private static int traverseForMinimum(int i, int j) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((e1, e2) -> Integer.compare(e1[0], e2[0]));
        pq.offer(new int[] {0, i, j});
        boolean[][] visited = new boolean[n][n];
        int count = 0;
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int diff = cur[0], row = cur[1], col = cur[2];
            if (visited[row][col])
                continue;
            visited[row][col] = true;
            if (diff > height)
                count += diff;
            for (int k = 0; k < 4; k++) {
                int nr = row + dr[k], nc = col + dc[k];
                if (0 > nr || nr >= n || 0 > nc || nc >= n || visited[nr][nc])
                    continue;
                diff = Math.abs(land[nr][nc] - land[row][col]);
                pq.offer(new int[] { diff, nr, nc});
            }
        }
        return count;
    }
}