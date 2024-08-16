import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        Queue<int[]> queue = new LinkedList(); // (total, idx)
        queue.offer(new int[] {numbers[0], 0});
        queue.offer(new int[] {-numbers[0], 0});
        while (queue.peek()[1] < numbers.length - 1) {
            int[] num = queue.poll();
            int nextNum = numbers[num[1] + 1];
            queue.offer(new int[] {num[0] + nextNum, num[1] + 1});
            queue.offer(new int[] {num[0] - nextNum, num[1] + 1});
        }
        for (int[] nums: queue) {
            if (nums[0] == target) 
                answer++;
        }
        return answer;
    }
}