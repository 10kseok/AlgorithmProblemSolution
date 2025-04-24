class Solution {
    static int answer;
    static String[] words;
    static boolean[] logs;

    public int solution(String begin, String target, String[] words) {
        Solution.answer = Integer.MAX_VALUE;
        Solution.words = words;
        Solution.logs = new boolean[words.length];
        dfs(0, begin, target);

        return answer == Integer.MAX_VALUE ? 0 : answer;
    }

    public static void dfs(int step, String word, String target) {
        if (word.equals(target)) {
            // Solution.logs[Solution.words.length - 1] = false;
            Solution.answer = Math.min(step, Solution.answer);
            return;
        }

        for (int i = 0; i < Solution.words.length; i++) {
            if (!Solution.logs[i] && validate(word, Solution.words[i])) {
                Solution.logs[i] = true;
                dfs(step + 1, Solution.words[i], target);
                Solution.logs[i] = false;
            }
        }
    }

    private static boolean validate(String a, String b) {
        int count = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) == b.charAt(i)) count++;
        }
        return count == a.length() - 1;
    }
}