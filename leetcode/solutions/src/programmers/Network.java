package programmers;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.IntStream;
import util.ArrayParser;

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/43162
 * 네트워크
 *
 * 여러개가 하나로 묶여진다고 생각하여 유니온 파인드를 공부해서 사용해본 문제.
 *
 * @author koesnam (추만석)
 * @since 2023.12.13
 */
public class Network {
//    private static int[] parents;
//    // Union-Find
//    public int solution(int n, int[][] computers) {
//        parents = IntStream.range(0, n).toArray();
//        for (int i = 0; i < computers.length; i++) {
//            for (int j = 0; j < computers[0].length ; j++) {
//                if (i == j) continue;
//                if (computers[i][j] == 1) {
//                    union(i, j);
//                }
//            }
//        }
//
//        Set<Integer> answer = new HashSet<>();
//        for (int i = 0; i < n; i++) {
//            answer.add(find(parents[i]));
//        }
//        return answer.size();
//    }
//
//    private static int find(int x) {
//        if (x == parents[x]) return x;
//        return parents[x] = find(parents[x]);
//    }
//
//    private static void union(int x, int y) {
//        x = find(x);
//        y = find(y);
//        if (x != y) parents[Math.max(x, y)] = Math.min(x, y);
//    }

    // Simple DFS
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(computers, visited, i);
                answer++;
            }
        }
        return answer;
    }

    public void dfs(int[][] computers, boolean[] visited, int startNode) {
        visited[startNode] = true;
        for (int i = 0; i < computers[0].length; i++) {
            if (computers[startNode][i] == 1 && !visited[i]) {
                dfs(computers, visited, i);
            }
        }
    }

    public static void main(String[] args) {
        Network network = new Network();
        System.out.println(network.solution(3, ArrayParser.parse("[[1, 1, 0], [1, 1, 0], [0, 0, 1]]")));
        System.out.println(network.solution(3, ArrayParser.parse("[[1, 1, 0], [1, 1, 1], [0, 1, 1]]")));
        System.out.println(network.solution(5, ArrayParser.parse("[[1, 0, 0, 0, 1], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]]")));
//        System.out.println(network.solution(5, ArrayParser.parse("[" +
//                " [1, 0, 0, 0, 0]," +
//                " [0, 1, 1, 0, 1]," +
//                " [0, 1, 1, 1, 1]," +
//                " [0, 0, 1, 1, 0]," +
//                " [1, 0, 1, 0, 1]," +
//                "]")));
    }
}
