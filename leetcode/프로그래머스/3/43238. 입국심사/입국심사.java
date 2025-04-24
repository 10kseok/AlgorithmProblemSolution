class Solution {
    public long solution(int n, int[] times) {
        int min = Integer.MAX_VALUE;
        for (int t : times) {
            if (t < min)
                min = t;
        }

        long lower = 1, upper = (long) min * n;
        while (lower <= upper) {
            long mid = (lower + upper) / 2;
            long _n = 0;
            for (int t : times) {
                _n += mid / t;
            }
            if (_n >= n) {
                upper = mid - 1;
            } else {
                lower = mid + 1;
            }
        }
        // System.out.println(String.format("lower %d, upper %d", lower, upper));
        return lower;
    }
}