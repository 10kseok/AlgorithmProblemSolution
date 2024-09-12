import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        Arrays.sort(A); Arrays.sort(B);
        
        // 1 3 5 7
        // 2 2 6 8
        int n = A.length;
        for (int i = 0, lastBiggestIdx = 0; i < n && lastBiggestIdx < n; i++) {
            if (A[i] >= B[lastBiggestIdx++]) {
                i--;
            } else {
                answer++;
            }
        }
        return answer;
    }
}