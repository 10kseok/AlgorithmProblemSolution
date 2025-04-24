import java.util.*;

class Solution {
    private static int n;
    private static int[] dx = new int[] {1, -1, 0, 0};
    private static int[] dy = new int[] {0, 0, 1, -1};
    private static int[][] game_board;
    private static int[][] table;
    
    public int solution(int[][] game_board, int[][] table) {
        int answer = 0;
        Solution.n = game_board.length;
        Solution.game_board = game_board;
        Solution.table = table;
        
        List<List<int[]>> blanks = new ArrayList();
        for (int i = 0; i < game_board.length; i++) {
            for (int j = 0; j < game_board[0].length; j++) {
                if (game_board[i][j] == 0) {
                    List<int[]> history = new ArrayList();
                    dfs(i, j, history);
                    blanks.add(history);
                }
            }
        }
        
        List<List<int[]>> patterns = new ArrayList();
        for (int i = 0; i < table.length; i++) {
            for (int j = 0; j < table[0].length; j++) {
                if (table[i][j] == 1) {
                    List<int[]> history = new ArrayList();
                    patternDfs(i, j, history);
                    patterns.add(history);
                }
            }
        }
        
        for (List<int[]> blank : blanks) {
            moveOriginForComparing(blank);
            Collections.sort(blank, (p1, p2) -> {
                return p1[0] == p2[0] ? p1[1] - p2[1] : p1[0] - p2[0];
            });
        }
        for (List<int[]> pattern : patterns) {
            moveOriginForComparing(pattern);
            Collections.sort(pattern, (p1, p2) -> {
                return p1[0] == p2[0] ? p1[1] - p2[1] : p1[0] - p2[0];
            });
        }
            
        // 패턴 매칭
        for (List<int[]> blank : blanks) {
            for (List<int[]> pattern : patterns) {
                if (blank.size() != pattern.size())
                    continue;
                if (match(blank, pattern)) {
                    answer += blank.size();
                    patterns.remove(pattern);
                    break;
                }
            }
        }
        
        return answer;
    }
    
    private static void dfs(int i, int j, List<int[]> history) {
        game_board[i][j] = 1;
        history.add(new int[] {i, j});
        for (int k = 0; k < 4; k++) {
            int nx = i + dx[k], ny = j + dy[k];
            if (0 <= nx && nx < n && 0 <= ny && ny < n && game_board[nx][ny] == 0)
                dfs(nx, ny, history);
        }
    }
    
    private static void patternDfs(int i, int j, List<int[]> history) {
        table[i][j] = 0;
        history.add(new int[] {i, j});
        for (int k = 0; k < 4; k++) {
            int nx = i + dx[k], ny = j + dy[k];
            if (0 <= nx && nx < n && 0 <= ny && ny < n && table[nx][ny] == 1)
                patternDfs(nx, ny, history);
        }
    }
    
    private static void moveOriginForComparing(List<int[]> positions) {
        int minX = Integer.MAX_VALUE, minY = Integer.MAX_VALUE;
        for (int[] pos : positions) {
            minX = Math.min(pos[0], minX);
            minY = Math.min(pos[1], minY);
        }
        
        for (int[] pos : positions) {
            pos[0] -= minX;
            pos[1] -= minY;
        }
    }
    
    private static List<int[]> rotate90(List<int[]> positions) {
        List<int[]> buffer = new ArrayList();
        int maxY = 0;
        for (int[] position : positions)
            maxY = Math.max(maxY, position[1]);
        for (int[] position : positions)
            buffer.add(new int[] {maxY - position[1], position[0]});
        Collections.sort(buffer, (p1, p2) -> {
                return p1[0] == p2[0] ? p1[1] - p2[1] : p1[0] - p2[0];
            });
        return buffer;
    }
    
    private static boolean match(List<int[]> blank, List<int[]> pattern) {
        int length = blank.size();
        boolean isSame = true;
        for (int i = 0; i < length; i++) {
            if (blank.get(i)[0] != pattern.get(i)[0] || blank.get(i)[1] != pattern.get(i)[1]) {
                isSame = false;
                break;
            }
        }
        if (isSame)
            return true;
        
        // 회전 시켰을 때도 고려! 90, 180, 270
        List<int[]> rotatedPattern = pattern;
        for (int rotateCnt = 0; rotateCnt < 3; rotateCnt++) {
            rotatedPattern = rotate90(rotatedPattern); 
            isSame = true;
            for (int i = 0; i < length; i++) {
                if (blank.get(i)[0] != rotatedPattern.get(i)[0] || blank.get(i)[1] != rotatedPattern.get(i)[1]) {
                    isSame = false;
                    break;
                }
            }
            if (isSame)
                return true;
        }
        
        return false;
    }
}