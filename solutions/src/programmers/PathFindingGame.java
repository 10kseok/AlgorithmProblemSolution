package programmers;

import java.util.*;

/**
 * PathFindingGame
 * https://school.programmers.co.kr/learn/courses/30/lessons/42892?language=java
 * 길 찾기 게임
 * 결과 : 주어진 노드를 전위 순회, 후위 순회한 결과를 반환해야한다.
 * 
 * 조건
 * nodeinfo[i] 는 i + 1번 노드의 좌표이며, [x축 좌표, y축 좌표] 순으로 들어있다.
 * nodeinfo의 y 좌표는 노드의 레벨을 말한다.
 * 
 * 풀이
 * 
 */
public class PathFindingGame {
    class Solution {
        public int[][] solution(int[][] nodeinfo) {
            Node[] nodes = new Node[nodeinfo.length];
            for (int i = 0; i < nodes.length; i++) {
                nodes[i] = new Node(i + 1, nodeinfo[i][0], nodeinfo[i][1]);
            }
            Arrays.sort(nodes);
            Tree tree = new Tree(nodes[0]);
            for (int i = 1; i < nodes.length; i++) {
                tree.addNode(nodes[i]);
            }

            List<Integer> preorderVisits = new ArrayList<>();
            List<Integer> postorderVisits = new ArrayList<>();

            tree.preorder(preorderVisits);
            tree.postorder(postorderVisits);

            return new int[][] {
                    preorderVisits
                            .stream()
                            .mapToInt(Integer::intValue)
                            .toArray(),
                    postorderVisits.stream()
                            .mapToInt(Integer::intValue)
                            .toArray()
            };
        }
    }

    static class Tree {
        private final Node root;

        public Tree(Node root) {
            this.root = root;
        }

        public void addNode(Node node) {
            Node curNode = root;
            while (curNode != null) {
                if (node.value > curNode.value) {
                    if (curNode.right == null) {
                        curNode.right = node;
                        break;
                    }
                    curNode = curNode.right;
                } else {
                    if (curNode.left == null) {
                        curNode.left = node;
                        break;
                    }
                    curNode = curNode.left;
                }
            }
        }

        public void preorder(List<Integer> visits) {
            preorder(visits, root);
        }

        public void preorder(List<Integer> visits, Node curNode) {
            if (curNode == null) {
                return;
            }
            visits.add(curNode.num);
            preorder(visits, curNode.left);
            preorder(visits, curNode.right);
        }

        public void postorder(List<Integer> visits) {
            postorder(visits, root);
        }

        public void postorder(List<Integer> visits, Node curNode) {
            if (curNode == null) {
                return;
            }
            postorder(visits, curNode.left);
            postorder(visits, curNode.right);
            visits.add(curNode.num);
        }
    }

    static class Node implements Comparable {
        private final int num;
        private final int value;
        private final int level;
        private Node left;
        private Node right;

        public Node(int num, int value, int level) {
            this.num = num;
            this.value = value;
            this.level = level;
        }

        @Override
        public int compareTo(Object o) {
            // 값은 오름차순, 차수는 내림차순
            if (this.level == ((Node) o).level) {
                return this.value - ((Node) o).value;
            }
            return ((Node) o).level - this.level;
        }
    }
}