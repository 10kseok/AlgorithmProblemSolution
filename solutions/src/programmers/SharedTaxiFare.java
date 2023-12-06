package programmers;

import java.util.Arrays;

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/72413
 * 합습 택시 요금
 *
 * 풀이
 * - 플로이드 워샬 알고리즘
 * - 정점이 다른 정점으로 가기 위한 최소 비용들을 구하는 데, 모든 정점에 대해서 계산한다.
 * ** 다익스트라와 차이점 **
 * : 다익스트라는 한 정점(출발지)을 기준으로 다른 정점(목적지)까지의 최소 비용을 구한다.
 *
 * @author koesnam (추만석)
 * @since 2023.12.01
 */
public class SharedTaxiFare {
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = Integer.MAX_VALUE;
        // 모든 비용들이 최대값으로만 구성되었을 경우
        int MAX_TOTAL_FARE = 100_000 * n;

        int[][] graph = new int[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            // 해당 노드는 '접근할 수 없는 노드'라는 의미로 MAX_TOTAL_FARE 보다 큰 값을 할당시킨다.
            Arrays.fill(graph[i], MAX_TOTAL_FARE + 1);
            graph[i][i] = 0;
        }

        for (int[] fare : fares) {
            graph[fare[0]][fare[1]] = graph[fare[1]][fare[0]] = fare[2];
        }

        // 경유지를 기준으로 모든 정점들에서의 최소비용을 구한다.
        for (int stopover = 1; stopover <= n; stopover++) {
            for (int dep = 1; dep <= n; dep++) {
                for (int dest = 1; dest <= n; dest++) {
                    graph[dep][dest] = Math.min(graph[dep][dest], graph[dep][stopover] + graph[stopover][dest]);
                }
            }
        }

        for (int stopover = 1; stopover <= n; stopover++) {
            answer = Math.min(answer, graph[s][stopover] + graph[stopover][a] + graph[stopover][b]);
        }
        return answer;
    }
}
