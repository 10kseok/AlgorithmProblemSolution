class Solution {
    public int[] solution(int brown, int yellow) {
        for (int x = yellow; x >= Math.sqrt(yellow); x--) {
            if (yellow % x != 0)
                continue;
            int y = yellow / x;
            if (brown == x*2 + y*2 + 4) {
                return new int[] {x + 2, y + 2};
            }
        }
        throw new RuntimeException("NEVER REACHED");
    }
}