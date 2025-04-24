package programmers;

/**
 * SecretMap
 */
public class SecretMap {
    
    public static String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = {};
        // logic


        return answer;
    }

    public static boolean validate(String[] expect, String[] result) {
        if (expect.length != result.length) return false;

        for (int i = 0; i < expect.length; i++) {
            if ((expect[i].compareTo(result[i])) == 0) return false;
        }

        return true;
    }

    public static void main(String[] args) {
        // int testN1 = 5;
        // int[] testArr1_1 = new int[] {9, 20, 28, 18, 11};
        // int[] testArr1_2 = new int[] {30, 1, 21, 17, 28};
        // String[] testResult1 = new String[] {"#####", "# # #",  "### #", "# ##", "#####"};
        
        // System.out.println(validate(testResult1, solution(testN1, testArr1_1, testArr1_2)));


        // int testN2 = 6;
        // int[] testArr2_1 = new int[] {46, 33, 33 ,22, 31, 50};
        // int[] testArr2_2 = new int[] {27 ,56, 19, 14, 14, 10};
        // String[] testResult2 = new String[] {"######", "### #", "## ##", " #### ", " #####", "### # "};

        // System.out.println(validate(testResult2, solution(testN2, testArr2_1, testArr2_2)));
        System.out.println(47 | 20);
    }
}