import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {
//    public static void main(String[] args) throws IOException {
//        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
//
//        reader.readLine();
//        int[] distance = Arrays.stream(reader.readLine().split("\\s"))
//                .mapToInt(Integer::parseInt)
//                .toArray();
//        int[] costsByCity = Arrays.stream(reader.readLine().split("\\s"))
//                .mapToInt(Integer::parseInt)
//                .toArray();
//
//        writer.write(String.valueOf(calculateMinimumOilCost(distance, costsByCity)));
//        reader.close();
//        writer.close();
//    }
//    private static long calculateMinimumOilCost(int[] distance, int[] costsByCity) {
//        long minimumCost = costsByCity[0];
//        long total = minimumCost * distance[0];
//        for (int i = 1; i < distance.length; i++) {
//            if (minimumCost > costsByCity[i]) minimumCost = costsByCity[i];
//            total += minimumCost * distance[i];
//        }
//        return total;
//    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        reader.readLine();
        int[] distance = splitAndReturn(new StringTokenizer(reader.readLine()));
        int[] costsByCity = splitAndReturn(new StringTokenizer(reader.readLine()));

        writer.write(String.valueOf(calculateMinimumOilCost(distance, costsByCity)));
        reader.close();
        writer.close();
    }

    private static long calculateMinimumOilCost(int[] distance, int[] costsByCity) {
        long minimumCost = costsByCity[0];
        long total = minimumCost * distance[0];
        for (int i = 1; i < distance.length; i++) {
            if (minimumCost > costsByCity[i]) minimumCost = costsByCity[i];
            total += minimumCost * distance[i];
        }
        return total;
    }

    private static int[] splitAndReturn(StringTokenizer tokenizer) {
        int[] result = new int[tokenizer.countTokens()];
        for (int i = 0; i < result.length; i++) {
            result[i] = Integer.parseInt(tokenizer.nextToken());
        }
        return result;
    }
}