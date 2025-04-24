package programmers;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/131127
 * 할인 행사
 * 
 * 풀이
 * 배열의 10칸 내에 원하는 만큼의 음식이 들어있는가
 */
public class DiscountEvent {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        for (int i = 0; i <= discount.length - 10; i++) {
            Counter counter = new Counter(Arrays.copyOfRange(discount, i, i+10));
            for (int j = 0; j < want.length; j++) {
                if (counter.getCount(want[j]) != number[j]) break;
                if (j == want.length - 1 && counter.getCount(want[j]) == number[j]) {
                    answer++;
                }
            }
        }
        return answer;
    }

    static class Counter {
        private Map<String, Integer> bucket;

        public Counter(String[] tendaysDiscount) {
            this.bucket = new HashMap<>(tendaysDiscount.length);
            for (String product : tendaysDiscount) {
                bucket.put(product, bucket.getOrDefault(product, 0) + 1);
            }
        }

        public int getCount(String product) {
            return bucket.getOrDefault(product, 0);
        }
    }
}
