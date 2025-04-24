package programmers;

import java.util.LinkedList;
import java.util.Queue;
import util.ArrayParser;

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/1844
 * 게임 맵 최단거리
 *
 * DFS 인 줄 알았으나, BFS 였던...!
 * DFS로 하면 정확성 테스트는 통과할 수 있으나, 효율성 테스트에선 실패한다.
 * DFS가 되면 모든 경로를 탐색하는데, 이 때 모든 경로라고 하면 특정 지점에서 4방향으로 뻗어지는 모든 경로를 말한다.
 * 따라서 특정 기준이 없다면 최악의 경우 시간복잡도가 O(2**N)이 될 수 있다.
 *
 * BFS를 이용하면 최소한의 탐색을 통해서 구할 수 있다.
 * 처음부터 최소 값들을 구해서 나아가기 때문에 최악의 경우에도 시간복잡도는 O(N)이 된다.
 *
 * @author koesnam (추만석)
 * @since 2023.12.12
 */
public class ShortestDistanceInGameMap {
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

    public static void main(String[] args) {
        ShortestDistanceInGameMap shortestDistanceInGameMap = new ShortestDistanceInGameMap();
        System.out.println(shortestDistanceInGameMap.solution(ArrayParser.parse("[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]")));
    }
}
