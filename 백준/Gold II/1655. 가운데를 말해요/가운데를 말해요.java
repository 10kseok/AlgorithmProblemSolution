import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringJoiner;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());
        int[] baekjoonSays = new int[N];
        for (int i = 0; i < N; i++) {
            baekjoonSays[i] = Integer.parseInt(reader.readLine());
        }

        writer.write(sayCenterNumberIn(baekjoonSays));
        reader.close();
        writer.close();
    }

    private static String sayCenterNumberIn(int[] baekjoonSays) {
        int midNum = baekjoonSays[0];
//        StringJoiner stringJoiner = new StringJoiner("\n");
//        stringJoiner.add(String.valueOf(midNum));
        StringBuilder sb = new StringBuilder();
        sb.append(midNum);
        sb.append("\n");
        PriorityQueue<Integer> smallerQueue = new PriorityQueue<>(Comparator.reverseOrder());
        PriorityQueue<Integer> largerQueue = new PriorityQueue<>();
        for (int i = 1; i < baekjoonSays.length; i++) {
            int curNum = baekjoonSays[i];
            if (curNum < midNum) smallerQueue.add(curNum);
            else largerQueue.add(curNum);

            if (largerQueue.size() - smallerQueue.size() > 1) {
                int newMid = largerQueue.poll();
                smallerQueue.add(midNum);
                midNum = newMid;
            }
            if (smallerQueue.size() > largerQueue.size()) {
                int newMid = smallerQueue.poll();
                largerQueue.add(midNum);
                midNum = newMid;
            }
//            stringJoiner.add(String.valueOf(midNum));
            sb.append(midNum);
            sb.append("\n");
        }
//        return stringJoiner.toString();
        return sb.toString();
    }
}