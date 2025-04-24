import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main {
    static int[][] heights;
    static int maxHeight;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());
        initHeights(N, reader);

        writer.write(searchSafeArea(N));
        reader.close();
        writer.close();
    }

    private static String searchSafeArea(int N) {
        int maxSafeAreaCount = 1;
        for (int h = 0; h < maxHeight; h++) {
            boolean[][] visited = new boolean[N][N];
            maxSafeAreaCount = Math.max(search(visited, h), maxSafeAreaCount);
        }
        return String.valueOf(maxSafeAreaCount);
    }

    private static int search(boolean[][] visited, int warningHeight) {
        int sectionCount = 0;
        for (int i = 0; i < heights.length; i++) {
            for (int j = 0; j < heights[0].length; j++) {
                if (!visited[i][j] && heights[i][j] > warningHeight) {
                    dfs(i, j, visited, warningHeight);
                    sectionCount += 1;
                }
            }
        }
        return sectionCount;
    }

    private static void dfs(int i, int j, boolean[][] visited, int warningHeight) {
        if (i < 0 || i >= heights.length
                || j < 0 || j >= heights[0].length
                || visited[i][j] || heights[i][j] <= warningHeight) return;

        visited[i][j] = true;

        dfs(i + 1, j, visited, warningHeight);
        dfs(i - 1, j, visited, warningHeight);
        dfs(i, j + 1, visited, warningHeight);
        dfs(i, j - 1, visited, warningHeight);
    }

    private static int[] splitAndReturn(StringTokenizer tokenizer) {
        int[] result = new int[tokenizer.countTokens()];
        for (int i = 0; i < result.length; i++) {
            int parsed = Integer.parseInt(tokenizer.nextToken());
            maxHeight = Math.max(parsed, maxHeight);
            result[i] = parsed;
        }
        return result;
    }

    private static void initHeights(int N, BufferedReader reader) throws IOException {
        heights = new int[N][N];
        for (int i = 0; i < N; i++) {
            heights[i] = splitAndReturn(new StringTokenizer(reader.readLine()));
        }
    }
}