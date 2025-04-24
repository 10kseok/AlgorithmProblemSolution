import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int answer = 0;
        for (int i = 0; i < citations.length; i++) {
            int h = citations[i];
            int greater = citations.length - i;
            answer = Math.max(answer, Math.min(h, greater));
        }
        return answer;
    }
}