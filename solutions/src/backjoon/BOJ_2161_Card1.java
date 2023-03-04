package backjoon;

import java.util.*;

/*
    1 ~ N 까지 순서대로 들어온 숫자가 순서대로 나가는 형태 -> Queue
 */
public class BOJ_2161_Card1 {
    public static void solution() {
        Scanner scanner = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        Queue<Integer> cards = new LinkedList<>();

        int cardCount = scanner.nextInt();

        for (int i = 1; i <= cardCount; i++) {
            cards.add(i);
        }

        while (cards.size() != 1) {
            sb.append(cards.remove()).append(' ');
            cards.add(cards.remove());
        }

        sb.append(cards.remove());
        System.out.println(sb);
    }
}

class Main {
    public static void main(String[] args) {
        BOJ_2161_Card1.solution();
    }
}
