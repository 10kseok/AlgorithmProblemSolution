import java.io.*;

class Main {
    private static int[] board;
    private static int count;
    private static int N;

    private static boolean isPromissing(int row) {
        for (int i = 0; i < row; i++) {
            if (board[i] == board[row] || Math.abs(row - i) == Math.abs(board[i] - board[row])) {
                return false;
            }
        }
        return true;
    }

    private static void searchQueen(int row) {
        if (row == N) {
            count++;
            return;
        }

        for (int col = 0; col < N; col++) {
            board[row] = col;
            if (isPromissing(row)) {
                searchQueen(row + 1);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(reader.readLine());
        count = 0;
        board = new int[N];
        searchQueen(0);

        writer.write(String.valueOf(count));

        reader.close();
        writer.close();
    }
}