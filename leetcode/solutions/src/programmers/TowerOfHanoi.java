package programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * TowerOfHanoi
 */
public class TowerOfHanoi {
    public int[][] solution(int n) {
        move(n, 1, 3, 2);
        return moved.stream()
                .map(l -> l.stream().mapToInt(Integer::intValue).toArray())
                .toArray(int[][]::new);
    }

    static List<List<Integer>> moved = new ArrayList<List<Integer>>();

    public static void move(int n, int start, int end, int stopover) {
        if (n == 1) {
            moved.add(List.of(start, end));
            return;
        }

        move(n - 1, start, stopover, end);
        moved.add(List.of(start, end));
        move(n - 1, stopover, end, start);
    }

    public static void main(String[] args) {
        TowerOfHanoi towerOfHanoi = new TowerOfHanoi();
        System.out.println(Arrays.deepToString(towerOfHanoi.solution(3)));
    }
}