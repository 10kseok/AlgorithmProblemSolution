package programmers;

import java.util.*;

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/86971
 * 완전탐색 > 전령망을 둘로 나누기
 * 
 * 목표 : 연결을 하나 끊어서 나눠진 전력망의 개수 차이가 작아야함.
 * 풀이 ( DFS 사용 )
 * 하나의 연결을 끊고 남는 연결들의 갯수 차이를 구한다.
 * 연결된 한 뭉치만 찾으면 남은 한 뭉치의 갯수를 알 수 있다.
 * (n - a1) + a1 = n ==> |a2 - a1| = (n - a1) - a1 = n - 2 * a1
 * 
 */
class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println("result : " + s.solution(9, new int[][] {{1, 3}, {2, 3}, {3, 4}, {4, 5}, {4, 6}, {4, 7}, {7, 8}, {7, 9}})); 
    }

    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        for (int[] excludedWire : wires) {
            Tree tree = new Tree(n);
            for (int[] wire : wires) {
                if (wire == excludedWire) continue;
                tree.add(wire[0], wire[1]);
            }
            answer = Math.min(answer, tree.evaluate());
        }
        return answer;
    }


    static class Tree {
        private Map<Integer, TreeNode> graph;

        public Tree(int n) {
            this.graph = new HashMap<>(n);
            for (int i = 1; i <= n; i++) {
                graph.put(i, new TreeNode(i));
            }
        }

        private void add(int nodeNum, int withNode) {
            graph.get(nodeNum).getConnections().add(withNode);
            graph.get(withNode).getConnections().add(nodeNum);
        }

        private TreeNode getNode(int treeNum) {
            return graph.get(treeNum);
        }

        public int evaluate() {
            Set<Integer> unions = new HashSet<>();
            evaluate(1, unions);
            // (n - a1) + a1 = n ==> |a2 - a1| = (n - a1) - a1 = n - 2 * a1
            return Math.abs(this.graph.size() - 2 * unions.size());
        }

        private void evaluate(int nodeNum, Set<Integer> unions) {
            TreeNode curNode = getNode(nodeNum);
            if (curNode.isVisited()) {
                return;
            }
            curNode.visit();
            List<Integer> otherNodeNums = curNode.getConnections();
            unions.addAll(otherNodeNums);
            for (int num : otherNodeNums) {
                evaluate(num, unions);
            }
        }

        static class TreeNode {
            private int nodeNum;
            private List<Integer> connections;
            private boolean isVisited;
            
            public TreeNode(int nodeNum) {
                this.nodeNum = nodeNum;
                this.connections = new ArrayList<>();
                this.connections.add(nodeNum);
                this.isVisited = false;
            }

            public List<Integer> getConnections() {
                return connections;
            }

            public void visit() {
                this.isVisited = true;
            }

            public boolean isVisited() {
                return isVisited;
            }
        }
    }
}