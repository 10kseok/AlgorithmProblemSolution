import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int A = Integer.parseInt(tokenizer.nextToken());
        int B = Integer.parseInt(tokenizer.nextToken());
        int C = Integer.parseInt(tokenizer.nextToken());

        writer.write(String.valueOf(power(A, B, C)));

        reader.close();
        writer.close();
    }

    private static int power(int A, int B, int C) {
        long answer = 1;
        long base = A;
        int multiplier = B;
        while (multiplier > 0) {
            if (multiplier % 2 == 1) {
                answer = answer * base % C;
            }
            base = base * base % C;
            multiplier /= 2;
        }
        return (int) answer;
    }
}