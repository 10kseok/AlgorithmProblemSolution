import java.util.*;

class Solution {
    private static Set<Integer> results = new HashSet();
    
    private static void permutation(String buffer, String numbers, boolean[] visited) {
        for (int j = 0; j < numbers.length(); j++) {
            if (!visited[j]) {
                visited[j] = true;
                String merged = buffer + numbers.charAt(j);
                results.add(Integer.valueOf(merged));
                permutation(merged, numbers, Arrays.copyOf(visited, visited.length));
                visited[j] = false;
            }
        }
    }
    
    private static boolean isPrimeNumber(int num) {
        if (num < 2) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0)
                return false;
        }
        return true;
    }
    public int solution(String numbers) {
        int answer = 0;
        // 나올 수 있는 숫자의 모든 경우를 구한다
        permutation("", numbers, new boolean[numbers.length()]);
        // 각 경우가 소수면 answer++
        for (Integer s: results) {
            if (isPrimeNumber(s))
                answer++;
        }
        return answer;
    }
}