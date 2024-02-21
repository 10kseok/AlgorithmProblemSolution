import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());
        List<Route> inputs = new ArrayList<>(N);
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(reader.readLine());
            int first = Integer.parseInt(st.nextToken());
            int second = Integer.parseInt(st.nextToken());
            inputs.add(new Route(first, second));
        }
        int d = Integer.parseInt(reader.readLine());

        writer.write(solution(N, d, inputs));
        reader.close();
        writer.close();
    }

    private static String solution(int N, int length, List<Route> routes) {
        routes.sort(null);
        // 범위 안에 있는 지점들을 담기 위한 최소힙
        PriorityQueue<Integer> minHeapOfHome = new PriorityQueue<>(N);
        int maxCount = 0;
        int count = 0;
        // 슬라이딩 윈도우와 유사. length 만큼의 윈도우를 다음 경로의 끝지점으로부터 앞으로 설정한다.
        for (Route route : routes) {
            int availableStartPoint = route.getEnd() - length;
            // 옮긴 범위안에 없으면 삭제
            while (!minHeapOfHome.isEmpty() && minHeapOfHome.peek() < availableStartPoint) {
                minHeapOfHome.poll();
                count--;
            }
            // 옮긴 범위안에 있으면 추가
            if (availableStartPoint <= route.getStart()) {
                count++;
                minHeapOfHome.add(route.getStart());
            }
            maxCount = Math.max(maxCount, count);
        }
        return String.valueOf(maxCount);
    }

    private static class Route implements Comparable<Route> {
        private final int start, end;

        public Route(int start, int end) {
            this.start = Math.min(start, end);
            this.end = Math.max(start, end);
        }

        public int getStart() {
            return start;
        }

        public int getEnd() {
            return end;
        }

        @Override
        public int compareTo(Route o) {
            if (end - o.getEnd() == 0) return Integer.compare(this.start, o.getStart());
            else return Integer.compare(this.end, o.getEnd());
        }
    }
}