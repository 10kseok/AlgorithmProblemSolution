package programmers;

import java.util.LinkedList;
import java.util.List;
import util.ArrayParser;

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/92343
 * 양과 늑대
 *
 * DFS를 하는데 특정 기준 도달시 다른 노드를 방문했다가 되돌아와서 탐색을 이어나간다.
 * 
 * @author koesnam (추만석)
 * @since 2023.12.11
 */
public class SheepAndWolf {
    static int[] info;
    static List<Integer>[] graph;
    public int solution(int[] info, int[][] edges) {
        SheepAndWolf.info = info;
        graph = new List[info.length];
        for (int i = 0; i < info.length; i++) {
            graph[i] = new LinkedList<>();
        }
        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
        }

        return dfs(0, 0, 0, graph[0]);
    }

    public static int dfs(int sheep, int wolf, int curNodeNum, List<Integer> nextNodes) {
        if (info[curNodeNum] == 0) sheep++;
        else if (sheep <= wolf + 1) return sheep;
        else wolf++;

        int answer = sheep;
        for (Integer node : nextNodes) {
            List<Integer> copiedNodes = new LinkedList<>(nextNodes);
            copiedNodes.remove(node);
            copiedNodes.addAll(graph[node]);
            answer = Math.max(answer, dfs(sheep, wolf, node, copiedNodes));
        }
        return answer;
    }

    public static void main(String[] args) {
        SheepAndWolf sheepAndWolf = new SheepAndWolf();
        System.out.println(sheepAndWolf.solution(new int[]{0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1}, ArrayParser.parse("[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]")));
    }
}
