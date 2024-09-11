import java.util.*;

class Solution {
    private static int[] profits;
    private static Map<String, Integer> nameToIdxMap;
    private static String[] referral;
    
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        Solution.profits = new int[enroll.length];
        Solution.nameToIdxMap = new HashMap(enroll.length);
        Solution.referral = referral;
        for (int i = 0; i < enroll.length; i++)
            nameToIdxMap.put(enroll[i], i);
        
        for (int i = 0; i < seller.length; i++) {
            dfs(nameToIdxMap.get(seller[i]), amount[i] * 100);
        }
        // center(root) 제외한 자식 노드들의 이익률!
        return profits;
    }
    
    private static void dfs(int idx, int profit) {
        int payment = profit / 10;
        profits[idx] += profit - payment;
        if (nameToIdxMap.get(referral[idx]) != null && profit > 0)
            dfs(nameToIdxMap.get(referral[idx]), payment);
    }
}