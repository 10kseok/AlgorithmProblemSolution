package backjoon.queue;

import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Scanner;

public class BOJ_25497 {
    public static void solution() {
        Scanner scanner = new Scanner(System.in);
        Deque<Character> stackLR = new ArrayDeque<>();
        Deque<Character> stackSK = new ArrayDeque<>();

        int n = Integer.parseInt(scanner.nextLine());
        String skills = scanner.nextLine();

        int count = 0;
        for (char skill : skills.toCharArray()) {
            switch (skill) {
                case 'L':
                    stackLR.addLast(skill);
                    break;
                case 'S':
                    stackSK.addLast(skill);
                    break;
                case 'R':
                    // 연계할 사전 기술 없이 본 기술을 사용했을 경우에는 게임의 스크립트가 꼬여서 이후 사용하는 기술들이 정상적으로 발동되지 않는다.
                    if (stackLR.isEmpty()) {
                        System.out.println(count);
                        return;
                    }
                    // 연계 기술은 사전 기술과 본 기술의 두 개의 개별 기술을 순서대로 사용해야만 정상적으로 사용 가능
                    stackLR.removeLast();
                    count++;
                    break;
                case 'K':
                    // 연계할 사전 기술 없이 본 기술을 사용했을 경우에는 게임의 스크립트가 꼬여서 이후 사용하는 기술들이 정상적으로 발동되지 않는다.
                    if (stackSK.isEmpty()) {
                        System.out.println(count);
                        return;
                    }
                    // 연계 기술은 사전 기술과 본 기술의 두 개의 개별 기술을 순서대로 사용해야만 정상적으로 사용 가능
                    stackSK.removeLast();
                    count++;
                    break;
                default:
                    count++;
                    break;
            }
        }
        System.out.println(count);
    }
}

//class Main {
//    public static void main(String[] args) {
//        BOJ_25497.solution();
//    }
//}
