import java.util.Queue;
import java.util.LinkedList;
import java.util.*;

class Solution {
    // 동, 서, 남, 북
    static int[] dx = new int[]{0, 0, 1, -1}; // 행
    static int[] dy = new int[]{1, -1, 0, 0}; // 열
    public int solution(int[][] maps) {
        int lastRowIdx = maps.length - 1;
        int lastColIdx = maps[0].length - 1;
        maps[lastRowIdx][lastColIdx] = -1;

        Queue<int[]> searchQ = new LinkedList<>();
        searchQ.add(new int[]{0, 0});

        while (!searchQ.isEmpty()) {
            int[] curPos = searchQ.poll();
            int x = curPos[0];
            int y = curPos[1];
            for (int i = 0; i < 4; i++) {
                int nextX = x + dx[i];
                int nextY = y + dy[i];
                if (nextX < 0 || nextX >= maps.length
                        || nextY < 0 || nextY >= maps[0].length
                        || maps[nextX][nextY] == 0) continue;
                
                if (maps[nextX][nextY] == 1 || maps[nextX][nextY] == -1) {
                    searchQ.add(new int[]{nextX, nextY});
                    maps[nextX][nextY] = maps[x][y] + 1;
                }
            }
        }
        return maps[lastRowIdx][lastColIdx];
    }
//     private static int[][] directions = new int[][] {
//         {  0,  1},
//         {  0, -1},
//         {  1,  0},
//         { -1,  0}
//     };
//     private static int[][] distance;
    
//     private static void dfs(int[][] maps, int i, int j) {
//         for (int[] direction: directions) {
//             int dx = i + direction[0], dy = j + direction[1];
//             if (dx < 0 || dx >= maps.length || dy < 0 || dy >= maps[0].length)
//                 continue;
//             if (maps[dx][dy] == 1 && distance[i][j] + 1 < distance[dx][dy]) {
//                 distance[dx][dy] = distance[i][j] + 1;
//                 dfs(maps, dx, dy);
//             }
//         }
//     }
//     public int solution(int[][] maps) {
//         distance = new int[maps.length][maps[0].length];
//         for (int i = 0; i < distance.length; i++) {
//             Arrays.fill(distance[i], 10_001);
//         }
//         distance[0][0] = 1;
//         dfs(maps, 0, 0);
//         int answer = distance[maps.length - 1][maps[0].length - 1];
//         return answer == 10_001 ? -1 : answer;
//     }
}