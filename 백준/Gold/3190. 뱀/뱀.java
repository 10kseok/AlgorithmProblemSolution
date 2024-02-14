import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {
    private static final int LEFT = 0;
    private static final int RIGHT = 1;
    private static final int ROW = 0;
    private static final int COL = 1;
    private static final int TIME = 0;
    private static final int ROTATE = 1;
    private static final int APPLE = 1;

    // 동, 서, 남, 북
    private static final int[] dr = new int[] {0, 0, 1, -1};
    private static final int[] dc = new int[] {1, -1, 0, 0};


    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());
        int[][] board = new int[N][N];

        int K = Integer.parseInt(reader.readLine());
        for (int i = 0; i < K; i++) {
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            int row = Integer.parseInt(tokenizer.nextToken()) - 1;
            int col = Integer.parseInt(tokenizer.nextToken()) - 1;
            board[row][col] = APPLE;
        }

        int L = Integer.parseInt(reader.readLine());
        Queue<int[]> directions = new LinkedList<>();
        for (int i = 0; i < L; i++) {
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            directions.add(
                new int[]{Integer.parseInt(tokenizer.nextToken()), tokenizer.nextToken().equals("D") ? RIGHT : LEFT}
            );
        }


        writer.write(String.valueOf(startDummyGame(board, directions)));

        reader.close();
        writer.close();
    }

    private static int startDummyGame(int[][] board, Queue<int[]> directions) {
        int time = 0;
        int curDirection = 0;
        int border = board.length;
        int[] DEFAULT_POS = new int[] {0, 0};
        Deque<int[]> snakeQueue = new LinkedList<>();
        snakeQueue.add(DEFAULT_POS);

        while (true) {
            int[] curPos = snakeQueue.peekFirst();
            assert curPos != null;
            int[] nextPos = new int[] {curPos[ROW] + dr[curDirection], curPos[COL] + dc[curDirection]};
            if (nextPos[ROW] < 0 || nextPos[ROW] >= border
                    || nextPos[COL] < 0 || nextPos[COL] >= border
                    || touchTail(snakeQueue, nextPos)) {
                time++;
                break;
            }
            snakeQueue.addFirst(nextPos);
            if (snakeQueue.size() != 1 && board[nextPos[ROW]][nextPos[COL]] != APPLE) snakeQueue.pollLast();
            if (board[nextPos[ROW]][nextPos[COL]] == APPLE) board[nextPos[ROW]][nextPos[COL]] = 0;
            time++;

            if (directions.peek() != null && directions.peek()[TIME] == time) {
                int rotate = directions.poll()[ROTATE];
                // 동, 서, 남, 북
                switch (curDirection) {
                    case 0:
                        // 동 -> 북, 남
                        curDirection = rotate == LEFT ? 3 : 2;
                        break;
                    case 1:
                        // 서 -> 남, 북
                        curDirection = rotate == LEFT ? 2 : 3;
                        break;
                    case 2:
                        // 남 -> 동, 서
                        curDirection = rotate == LEFT ? 0 : 1;
                        break;
                    case 3:
                        // 북 -> 서, 동
                        curDirection = rotate == LEFT ? 1 : 0;
                        break;
                }
            }
        }
        return time;
    }

    private static boolean touchTail(Queue<int[]> snakeQueue, int[] nextPos) {
        for (int[] body : snakeQueue) {
            if (body[ROW] == nextPos[ROW] && body[COL] == nextPos[COL]) return true;
        }
        return false;
    }
}