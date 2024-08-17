import java.util.*;

class Solution {
    private static boolean operate(int target, Set<Integer>[] table, int use, int operand1, int operand2) {
        Set<Integer> operand1Set = table[operand1];
        Set<Integer> operand2Set = table[operand2];
        Set<Integer> buffer = new HashSet();
        
        for (int n1 : operand1Set) {
            for (int n2 : operand2Set) {
                buffer.add(n1 + n2);
                buffer.add(n1 - n2);
                buffer.add(n1 * n2);
                if (n2 != 0)
                    buffer.add(n1 / n2);
            }
        }
        Set<Integer> origin = table[use];
        origin.addAll(buffer);
        return origin.contains(target);
    }
    public int solution(int N, int number) {
        if (N == number)
            return 1;
        Set<Integer>[] dp = new Set[9];
        dp[1] = Set.of(N);
        for (int i = 2; i < 9; i++) {
            dp[i] = new HashSet();
            for (int j = 1; j < i; j++) {
                if (operate(number, dp, i, j, i - j))
                    return i;
            }
            
            Set<Integer> origin = dp[i];
            int _n = N;
            for (int k = 1; k < i; k++)
                _n = _n * 10 + N;
            origin.add(_n);
            if (_n == number)
                return i;
        }
        return -1;
    }
}