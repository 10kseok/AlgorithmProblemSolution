import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;

public class BOJ_10814 {
    public static void solution() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(reader.readLine());
        ArrayList<String[]> peopleInfo = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] ageAndName = reader.readLine().split(" ");
            peopleInfo.add(ageAndName);
        }

        peopleInfo.sort(Comparator.comparingInt((String[] person) -> Integer.parseInt(person[0])));

        for (String[] person: peopleInfo) {
            writer.write(person[0] + " " + person[1] + "\n");
        }

        reader.close();
        writer.close();
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BOJ_10814.solution();
    }
}