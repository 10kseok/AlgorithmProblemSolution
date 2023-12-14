package programmers;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/43163
 * 단어 변환
 *
 * BFS! Not BTS
 * @author koesnam (추만석)
 * @since 2023.12.14
 */
public class WordConversion {
//    public int solution(String begin, String target, String[] words) {
//        if (Arrays.stream(words)
//                .noneMatch(word -> word.equals(target))) return 0;
//
//        int step = 0;
//        int n = begin.length();
//
//        Queue<List<String>> searchQ = new LinkedList<>();
//        searchQ.add(List.of(begin));
//
//        while (!searchQ.isEmpty()) {
//            List<String> similarities = new LinkedList<>();
//            List<String> available = searchQ.poll();
//            for (String curWord : available) {
//                if (curWord.equals(target)) return step;
//                for (String word : words) {
//                    int count = 0;
//                    for (int i = 0; i < n; i++) {
//                        if (curWord.charAt(i) == word.charAt(i)) count++;
//                    }
//                    if (count == n - 1) similarities.add(word);
//                }
//            }
//            searchQ.add(similarities);
//            step++;
//        }
//        return 0;
//    }

    // 1차 개선
    public int solution(String begin, String target, String[] words) {
        if (Arrays.stream(words)
                .noneMatch(word -> word.equals(target))) return 0;

        Logger logger = new Logger(words.length);
        Queue<Node> tree = new LinkedList<>();
        tree.offer(new Node(0, begin));

        while (!tree.isEmpty()) {
            Node curNode = tree.poll();
            if (curNode.data.equals(target)) return curNode.level;
            for (int i = 0; i < words.length; i++) {
                if (logger.hasLogAt(i)) continue;
                if (SimilarityValidator.validate(curNode.data, words[i])) {
                    tree.offer(new Node(curNode.level + 1, words[i]));
                    logger.log(i);
                }
            }
        }
        return 0;
    }

    static class Logger {
        private final boolean[] logs;

        public Logger(int n) {
            this.logs = new boolean[n];
        }

        void log(int i) {
            this.logs[i] = true;
        }

        boolean hasLogAt(int i) {
            return this.logs[i];
        }
    }

    static class SimilarityValidator {
        static boolean validate(String a, String b) {
            int count = 0;
            for (int i = 0; i < a.length(); i++) {
                if (a.charAt(i) == b.charAt(i)) count++;
            }
            return count == a.length() - 1;
        }
    }

    static class Node {
        private int level;
        private String data;

        public Node(int level, String data) {
            this.level = level;
            this.data = data;
        }
    }

    public static void main(String[] args) {
        WordConversion wordConversion = new WordConversion();
        System.out.println(wordConversion.solution("hit", "cog", new String[] {"hot", "dot", "dog", "lot", "log", "cog"}));
    }
}
