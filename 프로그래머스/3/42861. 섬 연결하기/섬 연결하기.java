import java.util.*;

class Solution {
    private static int[] parents;
    
    public int solution(int n, int[][] costs) {
        Solution.parents = new int[n];
        for (int i = 0; i < n; i++)
            Solution.parents[i] = i;
        
        Arrays.sort(costs, (c1, c2) -> Integer.compare(c1[2], c2[2]));
        Queue<int[]> graph = new LinkedList(Arrays.asList(costs));
        for (int[] cost : graph) {
            System.out.println(Arrays.toString(cost));
        }
        
        int tree_edges = 0, answer = 0;
        while (tree_edges < n - 1 && !graph.isEmpty()) {
            int[] edge = graph.poll();
            int u = edge[0], v = edge[1], cost = edge[2];
            int parentU = find(u), parentV = find(v);
            if (parentU != parentV) {
                union(parentU, parentV);
                answer += cost;
                tree_edges++;   
            }
        } 
        return answer;
    }
    
    private static int find(int x) {
        if (parents[x] == x)
            return parents[x];
        return parents[x] = find(parents[x]);
    }
    
    private static void union(int parentA, int parentB) {
        parents[Math.max(parentA, parentB)] = Math.min(parentA, parentB);
    }
}