package backjoon.sort;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.function.BinaryOperator;

public class BOJ_1181 {
    public static void solution() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(reader.readLine());
        ArrayList<String> words = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String word = reader.readLine();
            if (words.contains(word)) continue;
            words.add(word);
        }

        Collections.sort(words, (w1, w2) -> {
            if (w1.length() == w2.length()) return w1.compareTo(w2);
            return w1.length() - w2.length();
        });

        for (String word : words) {
            writer.write(word + "\n");
        }

        reader.close();
        writer.close();
    }
}

//class Main {
//    public static void main(String[] args) throws IOException {
//        BOJ_1181.solution();
//    }
//}
