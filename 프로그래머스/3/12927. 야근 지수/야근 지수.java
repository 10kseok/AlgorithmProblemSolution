import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        PriorityQueue<Integer> q = new PriorityQueue(Collections.reverseOrder());
        for (int work : works)
            q.offer(work);
        
        for (int i = 0; i < n; i++) {
            if (q.isEmpty() || q.peek() == 0)
                break;
            q.offer(q.poll() - 1);
        }
        
        long answer = 0;
        for (int work : q)
            answer += Math.pow(work, 2);
            
        return answer;
    }
}