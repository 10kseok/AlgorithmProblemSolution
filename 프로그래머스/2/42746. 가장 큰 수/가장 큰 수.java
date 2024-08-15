import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String[] strNumbers = new String[numbers.length];
        for (int i = 0; i < numbers.length; i ++) {
            strNumbers[i] = String.valueOf(numbers[i]);
        }
        Arrays.sort(strNumbers, (String x1, String x2) -> {
            return (x2 + x1).compareTo(x1 + x2);
        });
        
        if (strNumbers[0].equals("0"))
            return "0";
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < strNumbers.length; i++) {
            sb.append(strNumbers[i]);
        }
        String answer = sb.toString();
        return answer;
    }
}