import java.util.*;

class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int[][] map = new int[101][101];
        int BLANK = 0, IMPOSSIBLE = 2, AVAILABLE = 1;
        
        for (int[] rect : rectangle) {
            int x1 = rect[0], y1 = rect[1];
            int x2 = rect[2], y2 = rect[3];
            for (int i = 2 * x1; i <= 2 * x2; i++) {
                for (int j = 2 * y1; j <= 2 * y2; j++) {
                    if (2*x1 < i && i < 2*x2 && 2*y1 < j && j < 2*y2) {
                        map[i][j] = IMPOSSIBLE;
                        continue;
                    }
                    if ((i == 2*x1 || i == 2*x2 || j == 2*y1 || j == 2*y2) && map[i][j] == BLANK)
                        map[i][j] = AVAILABLE;
                }
            }
        }
        // for (int[] m : Arrays.copyOf(map, 20)) {
        //     System.out.println(Arrays.toString(Arrays.copyOf(m, 20)));
        // }
        
        // BFS
        Queue<int[]> queue = new LinkedList();
        int[][] directions = new int[][] {
            {  0,  1},
            {  0, -1},
            {  1,  0},
            { -1,  0}
        };
        queue.offer(new int[] { 2*characterX, 2*characterY, 0 });
        while (!queue.isEmpty()) {
            int[] curPos = queue.poll();
            int x = curPos[0], y = curPos[1];
            if (x == 2*itemX && y == 2*itemY) {
                return curPos[2] / 2;
            }
            for (int[] d : directions) {
                int dx = x + d[0], dy = y + d[1];
                if (dx < 0 || dx > 100 || dy < 0 || dy > 100 || map[dx][dy] != AVAILABLE)
                    continue;
                map[dx][dy] = BLANK;
                queue.offer(new int[] { dx, dy, curPos[2] + 1 });
            }
        }
        throw new RuntimeException("Unexpected Test Case");
    }
}