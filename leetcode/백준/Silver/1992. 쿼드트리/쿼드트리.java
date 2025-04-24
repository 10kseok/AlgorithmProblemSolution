import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());
        char[][] video = new char[N][N];

        for (int i = 0; i < N; i++) {
            video[i] = reader.readLine().toCharArray();
        }
        writer.write(compact(0, 0, N, video));

        reader.close();
        writer.close();
    }

    private static String compact(int startRow, int startCol, int n, char[][] video) {
        for (int i = startRow; i < startRow + n; i++) {
            for (int j = startCol; j < startCol + n; j++) {
                if (video[i][j] != video[startRow][startCol]) {
                    return "("
                            + compact(startRow, startCol, n / 2, video)
                            + compact(startRow, startCol + n / 2, n / 2, video)
                            + compact(startRow + n / 2, startCol, n / 2, video)
                            + compact(startRow + n / 2, startCol + n / 2, n / 2, video)
                            + ")";
                }
            }
        }
        return String.valueOf(video[startRow][startCol]);
    }
}