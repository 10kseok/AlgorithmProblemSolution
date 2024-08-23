import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        PriorityQueue<Integer> pQ = new PriorityQueue(Collections.reverseOrder());
        for (int prt: priorities)
            pQ.offer(prt);
        int[] locations = new int[priorities.length];
        Arrays.fill(locations, -1);
    
        int idx = 1;
        while (idx <= priorities.length) {
            for (int i = 0; i < priorities.length; i++) {
                if (priorities[i] == pQ.peek() && locations[i] == -1) {
                    pQ.poll();
                    locations[i] = idx;
                    idx++;
                    if (idx > priorities.length)
                        break;
                }
            }   
        }
        return locations[location];
    }
}