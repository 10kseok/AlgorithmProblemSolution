package backjoon.stack;

import java.io.*;
import java.util.Stack;

class BOJ_10828 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<Integer> stack = new Stack();

        int n = Integer.parseInt(reader.readLine());
        int result;
        String[] cmd;
        for (int i = 0; i < n; i++) {
            cmd = reader.readLine().split(" ");
            switch (cmd[0]) {
                case "push":
                    stack.push(Integer.parseInt(cmd[1]));
                    break;
                case "pop":
                    result = stack.empty() ? -1 : stack.pop();
                    writer.write(String.valueOf(result + "\n"));
                    break;
                case "size":
                    result = stack.size();
                    writer.write(String.valueOf(result + "\n"));
                    break;
                case "empty":
                    result = stack.empty() ? 1 : 0;
                    writer.write(String.valueOf(result) + "\n");
                    break;
                case "top":
                    result = stack.empty() ? -1 : stack.peek();
                    writer.write(String.valueOf(result + "\n"));
                    break;
            }
        }

        reader.close();
        writer.close();
    }
}