import java.util.*;

public class Solution {

    static List<Integer> info = new ArrayList<>();
    static List<Integer>[] G = new ArrayList[100001];
    static boolean[] vis = new boolean[100001];
    static int[] indegree = new int[100001];
    
    static int groupSize;
    static int group;

    // Constructor to initialize the graph adjacency list
    public Solution() {
        for (int i = 0; i < 100001; i++) {
            G[i] = new ArrayList<>();
        }
    }

    public static int test(int node) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int sum = 0;
        int sumSubtree = 0;
        vis[node] = true;

        for (int nxt : G[node]) {
            if (!vis[nxt]) {
                sumSubtree = test(nxt);
                sum += sumSubtree;
                pq.add(sumSubtree);
            }
        }

        while (!pq.isEmpty() && sum + info.get(node) > groupSize) { // current max size
            group++;
            sum -= pq.poll();
        }

        return sum + info.get(node);
    }

    public static int solution(int k, int[] num, int[][] links) {
        int n = num.length;
        int l = -1;
        int r = 0;

        // Initialize G, indegree, l, r
        for (int i = 0; i < n; i++) {
            info.add(num[i]);
            l = Math.max(l, num[i]);
            r += num[i];
            for (int j = 0; j < 2; j++) {
                if (links[i][j] != -1) {
                    G[i].add(links[i][j]);
                    indegree[links[i][j]]++;
                }
            }
        }

        // Find root
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                root = i;
                break;
            }
        }

        int ans = r;
        while (l < r) {
            Arrays.fill(vis, false);
            group = 0;

            groupSize = (l + r) / 2;
            test(root);

            if (group < k) {
                r = groupSize; // mid down -> group up
                ans = groupSize;
            } else {
                l = groupSize + 1; // mid up -> group down
            }
        }

        return ans;
    }
}
