package backjoon;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class BOJ_12873 {
    public static void solution() {
        try (Scanner scanner = new Scanner(System.in);) {
            int n = scanner.nextInt();
            // 삭제가 빈번하다 -> LinkedList를 이용하여 삭제시 소요되는 오버헤드를 줄인다.
            Queue<Integer> participants = IntStream
                    .rangeClosed(1, n)
                    .boxed()
                    .collect(Collectors.toCollection(LinkedList::new));

            int step = 1;
            while (participants.size() != 1) {
                long willExcludeIdx = (long) Math.pow(step, 3) - 1;
                int needMove = (int) (willExcludeIdx % participants.size());

                // 백준이 단계가 끝날 때까지 이동
                for (int i = 0; i < needMove; i++) {
                    participants.add(participants.poll());
                }
                // 참가자 제외
                participants.poll();
                // 다음 단계로 이동
                step++;
            }
            System.out.println(participants.peek());
        }
    }
}

class BOJ_12873_V2 {
    public static void solution() {
        try (Scanner scanner = new Scanner(System.in);) {
            int n = scanner.nextInt();
            // 삭제가 빈번하다 -> LinkedList를 이용하여 삭제시 소요되는 오버헤드를 줄인다.

            List<Integer> participantNumbers = IntStream
                    .rangeClosed(1, n)
                    .boxed()
                    .collect(Collectors.toCollection(LinkedList::new));
            
            // N명이 있으면 결국 N-1명이 제외되어야 끝난다! -> N-1번 연산이면 충분하다 -> 인덱스만 링버퍼로 산정해주면 끝 -> 동적으로 길이가 변해함으로 배열로는 불가능
            int curIdx = 0;
            for (int i = 1; i < n; i++) {
                long needMove = (long) Math.pow(i, 3) - 1;
                curIdx = (int) ((curIdx + needMove) % participantNumbers.size());
                participantNumbers.remove(curIdx);
            }
            System.out.println(participantNumbers.get(0));
        }
    }
}

class Main {
    public static void main(String[] args) {
        // BOJ_12873.solution();
        BOJ_12873_V2.solution();
    }
}
