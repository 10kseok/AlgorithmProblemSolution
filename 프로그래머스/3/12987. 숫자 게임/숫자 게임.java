import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        Arrays.sort(A); Arrays.sort(B);
        
        int n = A.length;
        for (int i = n - 1, lastBiggestIdx = n - 1; i >= 0; i--) {
            if (A[i] < B[lastBiggestIdx]) {
                answer++;
                lastBiggestIdx--;
            }
        }
        return answer;
    }
}