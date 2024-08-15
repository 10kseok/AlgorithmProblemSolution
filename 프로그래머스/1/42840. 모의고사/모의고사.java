import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] counter = {0, 0, 0};
        int[] pattern1 = new int[] {1, 2, 3, 4, 5};
        int[] pattern2 = new int[] {2, 1, 2, 3, 2, 4, 2, 5};
        int[] pattern3 = new int[] {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        for (int i = 0; i < answers.length; i++) {
            int ans = answers[i];
            if (ans == pattern1[i % pattern1.length]) {
                counter[0]++;   
            }
            if (ans == pattern2[i % pattern2.length]) {
                counter[1]++;   
            }
            if (ans == pattern3[i % pattern3.length]) {
                counter[2]++;   
            }
        }
        
        List<Integer> answer = new ArrayList();
        int winner = Math.max(Math.max(counter[0], counter[1]), counter[2]);
        for (int i = 0; i < 3; i++) {
            if (counter[i] == winner)
                answer.add(i + 1);
        }
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}