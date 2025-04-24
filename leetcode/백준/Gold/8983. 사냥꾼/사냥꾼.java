import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(reader.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        List<Integer> inputs1 = new ArrayList<>(M);
        st = new StringTokenizer(reader.readLine());
        for (int i = 0; i < M; i++) inputs1.add(Integer.parseInt(st.nextToken()));
        List<int[]> inputs2 = new ArrayList<>(N);
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(reader.readLine());
            inputs2.add(new int[]{Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())});
        }

        writer.write(solution(M, N, L, inputs1, inputs2));
        reader.close();
        writer.close();
    }

    private static String solution(int M, int N, int L, List<Integer> launchingPads, List<int[]> animals) {
        Collections.sort(launchingPads);
        int huntableCount = 0;
        for (int[] animal : animals) {
            // |a - x| + b <= L
            // = |a - x| <= L - b
            // = -L + b <= a - x <= L - b
            // = -L + b +- a <= -x <= L - b - a
            // = a + b - L <= x <= a - b + L
            int inclusiveMin = animal[0] + animal[1] - L ;
            int inclusiveMax = animal[0] - animal[1] + L ;
            if (rangeSearch(launchingPads, 0, launchingPads.size(), inclusiveMin, inclusiveMax)) {
                huntableCount++;
            }
        }
        return String.valueOf(huntableCount);
    }

    private static boolean rangeSearch(List<Integer> launchingPads, int fromIndex, int toIndex, int inclusiveMin, int inclusiveMax) {
        int low = fromIndex;
        int high = toIndex - 1;

        while (low <= high) {
            int mid = (low + high) >>> 1;
            int midVal = launchingPads.get(mid);

            if (midVal < inclusiveMin)
                low = mid + 1;
            else if (midVal > inclusiveMax)
                high = mid - 1;
            else
                // 최소값보다 크고 최대값보다 작은 경우! 범위 안에 들어와있는 경우를 말함.
                return true;
        }
        return false;
    }
}