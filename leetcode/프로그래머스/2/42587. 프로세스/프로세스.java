import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        PriorityQueue<Integer> pQ = new PriorityQueue(Collections.reverseOrder());
        for (int prt: priorities)
            pQ.offer(prt);
    
        int idx = 1;
        while (idx <= priorities.length) {
            for (int i = 0; i < priorities.length; i++) {
                if (priorities[i] == pQ.peek()) {
                    if (i == location)
                        return idx;
                    pQ.poll();
                    idx++;
                }
            }   
        }
        throw new RuntimeException("UNEXPECTED INPUTS");
    }
}