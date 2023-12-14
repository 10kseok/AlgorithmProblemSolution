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
    public int solution(String begin, String target, String[] words) {
        if (Arrays.stream(words)
                .noneMatch(word -> word.equals(target))) return 0;

        int step = 0;
        int n = begin.length();

        Queue<List<String>> searchQ = new LinkedList<>();
        searchQ.add(List.of(begin));

        while (!searchQ.isEmpty()) {
            List<String> similarities = new LinkedList<>();
            List<String> available = searchQ.poll();
            for (String curWord : available) {
                if (curWord.equals(target)) return step;
                for (String word : words) {
                    int count = 0;
                    for (int i = 0; i < n; i++) {
                        if (curWord.charAt(i) == word.charAt(i)) count++;
                    }
                    if (count == n - 1) similarities.add(word);
                }
            }
            searchQ.add(similarities);
            step++;
        }
        return 0;
    }

    public static void main(String[] args) {
        WordConversion wordConversion = new WordConversion();
        System.out.println(wordConversion.solution("hit", "cog", new String[] {"hot", "dot", "dog", "lot", "log", "cog"}));
    }
}
