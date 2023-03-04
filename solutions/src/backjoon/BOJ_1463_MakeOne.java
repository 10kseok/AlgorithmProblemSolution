package backjoon;

import java.util.Scanner;
/*
    연산 횟수의 최소값을 구해야하는 문제
    Bottom-up 방식으로 작은 값의 결과를 통해 큰 값의 결과를 구할 수 있다.
    2와 3으로 나눠 떨어지는 지 확인 후 나눠떨어진 숫자의 연산횟수에서 1(나누기연산)을 더한다.
    숫자테이블에서 각 인덱스별로 숫자에 맞는 최소 연산횟수를 할당한다.
    ex) 숫자    : x 1 2 3 4 5 6 7 8 9 10
        연산횟수 : x 0 1 1 2 3 2 2 3 2 3
 */
public class BOJ_1463_MakeOne {
    public static void solution() {
        Scanner scanner = new Scanner(System.in);
        int inputNum = scanner.nextInt();

        int[] numberTable = new int[inputNum + 1]; // 배열의 인덱스와 숫자를 매칭하기위해 사이즈를 1 늘려서 사용한다.
        numberTable[1] = 0;
        for (int i = 2; i < numberTable.length; i++) {
            int minOperatingCount = inputNum;
            if (i % 3 == 0) {
                minOperatingCount = Math.min(numberTable[i / 3], minOperatingCount);
            }
            if (i % 2 == 0) {
                minOperatingCount = Math.min(numberTable[i / 2], minOperatingCount);
            }
            minOperatingCount = Math.min(numberTable[i - 1], minOperatingCount);

            numberTable[i] = ++minOperatingCount; // 위에 세 연산 중 하나를 통해 구해진 결과이므로 +1
        }
        scanner.close();

        System.out.println(numberTable[inputNum]);
    }
}

class Main {
    public static void main(String[] args) {
        BOJ_1463_MakeOne.solution();
    }
}

