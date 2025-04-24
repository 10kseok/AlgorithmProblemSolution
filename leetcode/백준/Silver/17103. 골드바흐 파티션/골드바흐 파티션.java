import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

class Main {
    private static int MAX = 1_000_001;
    private static boolean[] isPrimeNumbers = new boolean[MAX];

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());
        int[] inputs = input(N, reader);

        writer.write(solution(N, inputs));
        reader.close();
        writer.close();
    }

    private static int[] input(int N, BufferedReader reader) throws IOException {
        int[] inputs = new int[N];
        for (int i = 0; i < N; i++) {
            inputs[i] = Integer.parseInt(reader.readLine());
        }
        return inputs;
    }

    private static String solution(int N, int[] evens) {
        Arrays.fill(isPrimeNumbers, true);
        isPrimeNumbers[0] = false;
        isPrimeNumbers[1] = false;

        for (int i = 2; i < MAX; i++) {
            if (isPrimeNumbers[i]) {
                for (int j = i + i; j < MAX; j += i) {
                    isPrimeNumbers[j] = false;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int even : evens) {
            int partionCount = 0;
            for (int i = 2; i <= even / 2; i++) {
                if (isPrimeNumbers[i] && isPrimeNumbers[even - i]) partionCount++;
            }
            sb.append(partionCount);
            sb.append("\n");
        }
        return sb.toString();
    }
}