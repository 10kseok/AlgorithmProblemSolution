import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());
        int[] times = Arrays.stream(reader.readLine().split("\\s"))
                .mapToInt(Integer::parseInt)
                .toArray();

        writer.write(String.valueOf(calculateMinimumWaitingTime(N, times)));
        reader.close();
        writer.close();
    }

    private static int calculateMinimumWaitingTime(int N, int[] times) {
        Arrays.sort(times);
        int[] accumulatedTimeTable = new int[N];
        accumulatedTimeTable[0] = times[0];

        for (int i = 1; i < N; i++) {
            accumulatedTimeTable[i] = times[i] + accumulatedTimeTable[i - 1];
        }
        return Arrays.stream(accumulatedTimeTable)
                .sum();
    }

}