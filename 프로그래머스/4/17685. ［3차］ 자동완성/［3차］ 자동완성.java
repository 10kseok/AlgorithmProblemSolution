import java.util.*;

class Solution {
    public int solution(String[] words) {
        Map<Character, Node> root = new HashMap(words.length);
        
        for (String word : words) {
            char[] cWord = word.toCharArray();
            Node prevNode = root.computeIfAbsent(cWord[0], c -> new Node(cWord[0]));
            
            for (int i = 1; i < cWord.length; i++) {
                if (prevNode.get(cWord[i]) != null) {
                    prevNode = prevNode.get(cWord[i]);
                    continue;
                }
                prevNode = prevNode.addNode(new Node(cWord[i]));
            }
            prevNode.isEnd = true;
        }
        
        int answer = 0;
        for (String word : words)
            answer += traversal(root.get(word.charAt(0)), word);
        return answer;
    }
    
    private static int traversal(Node root, String word) {
        int count = 1;
        Node node = root;
        
        for (int i = 1; i < word.length(); i++) {
            node = node.get(word.charAt(i));
            count++;
        }
        if (node.latters.size() > 0)
            return count;
        
        while (node != null && node.prevNode != null) {
            node = node.prevNode;
            if (!node.isEnd && node.latters.size() == 1)
                count--;
            else
                break;
        }
        
        return count;
    }
    
    class Node {
        Character letter;
        Map<Character, Node> latters;
        Node prevNode;
        boolean isEnd;
        
        public Node(Character letter) {
            this.letter = letter;
            this.latters = new HashMap();
            this.isEnd = false;
            this.prevNode = null;
        }
        
        public Node addNode(Node node) {
            this.latters.put(node.letter, node);
            node.prevNode = this;
            return node;
        }
        
        public Node get(Character key) {
            return this.latters.get(key);
        }
        
        // public void print() {
        //     System.out.println("parent Node " + letter + " --------");
        //     for (Node n : latters.values()) {
        //         System.out.println("latters Node " + n.letter);
        //     }
        //     System.out.println("-------------------------");            
        // }
    }
}

// g - [o, u] 
//             o - [n] n - [e] e - []
//             u - [i] i - [l] l - [d] d - []