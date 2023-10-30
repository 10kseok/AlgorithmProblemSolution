package backjoon.stack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 각 책더미에서 책번호가 아래에서 위로 갈수록 작아지는 구조라면 순차적임을 보장한다.
 */
public class BOJ_23253 {
    public static void solution() throws IOException {
        // scanner.nextInt()을 StringTokenizer로 변경 + Stack에서 int하나로 변경 --> 실행시간 1/4로 단축
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

        tokenizer.nextToken(); // 책의 총갯수는 사용하지 않으므로 따로 할당x
        int numberOfDummy = Integer.parseInt(tokenizer.nextToken());

        for (int i = 0; i < numberOfDummy; i++) {
            int lastBookIdx = Integer.MAX_VALUE;
            int numberOfBooks = Integer.parseInt(reader.readLine());
            tokenizer = new StringTokenizer(reader.readLine());
            do {
                int bookIdx = Integer.parseInt(tokenizer.nextToken());
                if (lastBookIdx < bookIdx) {
                    System.out.println("No");
                    return;
                }
                lastBookIdx = bookIdx;
            } while (--numberOfBooks > 0);
        }
        System.out.println("Yes");


        // 잘못된 예
//        Scanner scanner = new Scanner(System.in);
//        int totalNumberOfBooks = scanner.nextInt();
//        int numberOfDummy = scanner.nextInt();
//
//        ArrayList<Deque> dummyList = new ArrayList<>(numberOfDummy);
//        // input -> dummylist
//        for (int i = 0; i < numberOfDummy; i++) {
//            int numberOfBooks = scanner.nextInt();
//            Deque<Integer> dummy = new ArrayDeque();
//            for (int j = 0; j < numberOfBooks; j++) {
//                dummy.addLast(scanner.nextInt());
//            }
//            dummyList.add(dummy);
//        }
//
//        // check sequential
//        for (int i = 1; i <= totalNumberOfBooks; i++) {
//            for (Deque<Integer> dummy : dummyList) {
////                if (dummy.isEmpty()) continue;
//                Deque<Integer> testDummy = dummy;
//                if (dummy.peekLast() != null && dummy.peekLast() == i) dummy.removeLast();
//            }
//        }
//
//        System.out.println(
//                dummyList
//                        .stream()
//                        .map(Deque::size)
//                        .mapToInt(Integer::intValue)
//                        .sum() == 0 ? "Yes" : "No"
//        );
    }
}


class Main {
    public static void main(String[] args) throws IOException {
        BOJ_23253.solution();
    }

}
