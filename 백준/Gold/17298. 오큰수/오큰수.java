import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException{
		try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in));) {
			int s = Integer.parseInt(br.readLine());
			int[] seq = new int[s];

			StringTokenizer st = new StringTokenizer(br.readLine()); 
			for (int i = 0; i < s; i++)
				seq[i] = Integer.parseInt(st.nextToken());
			
			Deque<Integer> stack = new LinkedList<>();
			for (int i = s - 1; i >= 0; i--) {
				int element = seq[i];
				while (!stack.isEmpty() && stack.peek() <= element) {
					stack.pop();
				}
				seq[i] = stack.isEmpty() ? -1 : stack.peek();
				stack.push(element);
			}
			
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < s; i++)
				sb.append(seq[i]).append(" ");
			System.out.println(sb);
		} catch (Exception e) {
			throw e;
		}
	}
}