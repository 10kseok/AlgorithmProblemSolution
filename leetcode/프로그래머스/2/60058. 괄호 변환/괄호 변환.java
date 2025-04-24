import java.util.*;

class Solution {
    private static boolean isCorrect(String w) {
        int stack = 0;
        for (char c : w.toCharArray()) {
            if (c == '(')
                stack++;
            else {
                if (stack == 0)
                    return false;
                stack--;
            }
        }
        return stack == 0;
    }
    
    private static String divide(String w) {
        if (w.equals(""))
            return "";
        
        int leftCount = 0, rightCount = 0;
        char[] ws = w.toCharArray();
        String u = "", v = "";
        for (int i = 0; i < ws.length; i++) {
            if (ws[i] == '(')
                leftCount++;
            else
                rightCount++;
            if (rightCount == leftCount) {
                u = w.substring(0, i + 1);
                v = w.substring(i + 1);
                break;
            } 
        }
        
        if (isCorrect(u)) {
            return u + divide(v);
        }
        
        String vPlus = '(' + divide(v) + ')';
        String uPlus = "";
        for (int i = 1; i < u.length() - 1; i++)
            uPlus += u.charAt(i) == '(' ? ')' : '(';
        return vPlus + uPlus;
    }
    
    public String solution(String p) {
        if (isCorrect(p)) {
            return p;
        }
        String answer = divide(p);
        return answer;
    }
}