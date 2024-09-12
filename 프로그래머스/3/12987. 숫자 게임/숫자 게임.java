import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        Arrays.sort(A); Arrays.sort(B);
        
        // 1 3 5 7
        // 2 2 6 8
        int n = A.length;
        int lastBiggestIdx = 0;
        for (int i = 0; i < n; i++) {
            while (lastBiggestIdx < n && A[i] >= B[lastBiggestIdx])
                lastBiggestIdx++;
            if (lastBiggestIdx < n && A[i] < B[lastBiggestIdx]) {
                answer++;
                lastBiggestIdx++;
            }
        }
        return answer;
    }
}