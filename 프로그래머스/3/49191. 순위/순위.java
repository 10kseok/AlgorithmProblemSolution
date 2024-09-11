import java.util.*;

class Solution {
    private static int N;
    private static List<Integer>[] winnerResult;
    private static List<Integer>[] loserResult;
    
    public int solution(int n, int[][] results) {
        Solution.N = n;
        Solution.winnerResult = new List[n + 1]; // 자신이 이긴 결과
        Solution.loserResult = new List[n + 1]; // 자신이 졌던 결과
        
        for (int i = 1; i < n + 1; i++) {
            winnerResult[i] = new ArrayList();
            loserResult[i] = new ArrayList();
        }
            
        for (int[] result : results) {
            int winner = result[0], loser = result[1];
            winnerResult[winner].add(loser);
            loserResult[loser].add(winner);
        }
        
        int answer = 0;
        for (int i = 1; i < n + 1; i++) {
            int result = countAllResult(i);
            System.out.println(i + " |  result : " + result);
            if (countAllResult(i) == n)
                answer++;
        }
        return answer;
    }
    
    private static int countAllResult(int player) {
        int count = 1;
        Queue<Integer> q = new LinkedList();
        q.offer(player);
        boolean[] visited = new boolean[N + 1];
        
        while (!q.isEmpty()) {
            int p = q.poll();
            for (int loser : winnerResult[p]) {
                if (!visited[loser]) {
                    visited[loser] = true;
                    q.offer(loser);
                    count++;
                }
            }
        }
        
        q.offer(player);
        while (!q.isEmpty()) {
            int p = q.poll();
            for (int winner : loserResult[p]) {
                if (!visited[winner]) {
                    visited[winner] = true;
                    q.offer(winner);
                    count++;
                }
            }
        }
        return count;
    }
}