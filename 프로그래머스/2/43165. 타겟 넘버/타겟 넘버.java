import java.util.*;

class Solution {
    private static int[] _numbers;
    private static int answer;
    
    private static int dfs(int idx, int target, int total) {
        if (idx == _numbers.length) {
            return target == total ? 1 : 0;
        }
        return dfs(idx + 1, target, total + _numbers[idx]) + dfs(idx + 1, target, total - _numbers[idx]);
    }
    
    public int solution(int[] numbers, int target) {
        _numbers = numbers;
        return dfs(0, target, 0);
    }
    
//     public int solution(int[] numbers, int target) {
//         int answer = 0;
//         // Queue<int[]> queue = new LinkedList(); // (total, idx)
//         // queue.offer(new int[] {numbers[0], 0});
//         // queue.offer(new int[] {-numbers[0], 0});
//         // while (queue.peek()[1] < numbers.length - 1) {
//         //     int[] num = queue.poll();
//         //     int nextNum = numbers[num[1] + 1];
//         //     queue.offer(new int[] {num[0] + nextNum, num[1] + 1});
//         //     queue.offer(new int[] {num[0] - nextNum, num[1] + 1});
//         // }
//         // for (int[] nums: queue) {
//         //     if (nums[0] == target) 
//         //         answer++;
//         // }
//         return answer;
//     }
}