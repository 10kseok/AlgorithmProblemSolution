class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int tLength = t.chars().toArray().length;
        int pLength = p.chars().toArray().length;
        long pNumber = Long.valueOf(p);
        for (int i = 0; i <= tLength - pLength; i++) {
            long tNumber = Long.valueOf(t.substring(i, i + pLength));
            if (tNumber <= pNumber)
                answer += 1;   
        }
        
        return answer;
    }
}