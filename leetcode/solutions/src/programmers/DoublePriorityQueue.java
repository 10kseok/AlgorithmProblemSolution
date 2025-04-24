package programmers;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Optional;
import java.util.PriorityQueue;

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/42628
 * 이중우선순위큐
 *
 * @author koesnam (추만석)
 * @since 2023.12.15
 */
public class DoublePriorityQueue {
    // PriorityQueue를 사용한 풀이
//    public int[] solution(String[] operations) {
//        DoublePQ doublePQ = new DoublePQ();
//        for (String op : operations) {
//            String[] cmds = op.split(" ");
//            switch (cmds[0]) {
//                case "I":
//                    doublePQ.offer(Integer.parseInt(cmds[1]));
//                    break;
//                case "D":
//                    doublePQ.poll(cmds[1]);
//                    break;
//            }
//        }
//        return doublePQ.toAnswer();
//    }

    private static class DoublePQ {
        private final PriorityQueue<Integer> minHeap;
        private final PriorityQueue<Integer> maxHeap;

        public DoublePQ() {
            this.minHeap = new PriorityQueue<>();
            this.maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        }

        public void offer(int num) {
            minHeap.offer(num);
            maxHeap.offer(num);
        }

        public void poll(String cmd) {
            if (cmd.equals("-1")) maxHeap.remove(minHeap.poll());
            else if (cmd.equals("1")) minHeap.remove(maxHeap.poll());
        }

        public int[] toAnswer() {
            return new int[]{
                    Optional.ofNullable(maxHeap.poll()).orElse(0),
                    Optional.ofNullable(minHeap.poll()).orElse(0)
            };
        }
    }

    // PriorityQueue를 직접 구현한 느낌
    public int[] solution(String[] operations) {
        List<Integer> answer = new LinkedList<>();
        for (String op : operations) {
            String[] cmds = op.split(" ");
            switch (cmds[0]) {
                case "I":
                    answer.add(Integer.valueOf(cmds[1]));
                    break;
                case "D":
                    if (answer.isEmpty()) break;
                    Collections.sort(answer);
                    switch (cmds[1]) {
                        case "-1":
                            answer.remove(0);
                            break;
                        case "1":
                            answer.remove(answer.size() - 1);
                            break;
                    }
                    break;
            }
        }
        Collections.sort(answer); // 삭제 후에 삽입 됐을 경우도 정렬 ( TC 1번, TC 2번 )
        return answer.isEmpty() ? new int[]{0, 0} : new int[]{answer.get(answer.size() - 1), answer.get(0)};
    }

}
