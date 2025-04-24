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

    // 동(0도), 북(90도), 서(180도), 남(270도)
    private static final int[] dr = new int[] {0, -1, 0, 1};
    private static final int[] dc = new int[] {1, 0, -1, 0};


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


//        writer.write(String.valueOf(startDummyGame(board, directions)));
        writer.write(String.valueOf(startDummyGameWithTryExcept(board, directions)));

        reader.close();
        writer.close();
    }

//    private static int startDummyGame(int[][] board, Queue<int[]> directions) {
//        int time = 0;
//        int curDirection = 0;
//        int border = board.length;
//        Deque<int[]> snakeQueue = new LinkedList<>();
//        snakeQueue.add(new int[] {0, 0});
//
//        while (true) {
//            int[] curPos = snakeQueue.peekFirst();
//            assert curPos != null;
//            int[] nextPos = new int[] {curPos[ROW] + dr[curDirection], curPos[COL] + dc[curDirection]};
//            if (nextPos[ROW] < 0 || nextPos[ROW] >= border
//                    || nextPos[COL] < 0 || nextPos[COL] >= border
//                    || touchTail(snakeQueue, nextPos)) {
//                time++;
//                break;
//            }
//            snakeQueue.addFirst(nextPos);
//            if (snakeQueue.size() != 1 && board[nextPos[ROW]][nextPos[COL]] != APPLE) snakeQueue.pollLast();
//            if (board[nextPos[ROW]][nextPos[COL]] == APPLE) board[nextPos[ROW]][nextPos[COL]] = 0;
//            time++;
//            curDirection = changeDirectionIfNeeded(directions, time, curDirection);
//        }
//        return time;
//    }

    private static int startDummyGameWithTryExcept(int[][] board, Queue<int[]> directions) {
        int time = 0;
        int curDirection = 0;
        Deque<int[]> snakeQueue = new LinkedList<>();
        snakeQueue.add(new int[] {0, 0});

        try {
            while (true) {
                int[] curPos = snakeQueue.peekFirst();
                assert curPos != null;
                int[] nextPos = new int[] {curPos[ROW] + dr[curDirection], curPos[COL] + dc[curDirection]};
                if (touchTail(snakeQueue, nextPos)) throw new RuntimeException();
                snakeQueue.addFirst(nextPos);
                if (snakeQueue.size() != 1 && board[nextPos[ROW]][nextPos[COL]] != APPLE) snakeQueue.pollLast();
                if (board[nextPos[ROW]][nextPos[COL]] == APPLE) board[nextPos[ROW]][nextPos[COL]] = 0;
                time++;
                curDirection = changeDirectionIfNeeded(directions, time, curDirection);
            }
        } catch (Throwable e) {
            time++;
        }
        return time;
    }

    private static int changeDirectionIfNeeded(Queue<int[]> directions, int time, Integer curDirection) {
        if (directions.peek() != null && directions.peek()[TIME] == time) {
            int rotate = directions.poll()[ROTATE];
            curDirection = (rotate == LEFT ? curDirection + 1 : curDirection + 3) % 4;
        }
        return curDirection;
    }

    private static boolean touchTail(Queue<int[]> snakeQueue, int[] nextPos) {
        for (int[] body : snakeQueue) {
            if (body[ROW] == nextPos[ROW] && body[COL] == nextPos[COL]) return true;
        }
        return false;
    }
}