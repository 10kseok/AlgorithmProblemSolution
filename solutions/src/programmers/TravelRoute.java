package programmers;

import java.util.Arrays;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.stream.Collectors;
import util.ArrayParser;

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/43164
 * 여행경로
 * <p>
 * https://leetcode.com/problems/reconstruct-itinerary/description/
 * 리트코드에 해당 문제에 대한 더 자세한 테스트 케이스가 나와있다.
 *
 * @author koesnam (추만석)
 * @since 2023.12.14
 */
public class TravelRoute {
    /**
     * Programmers O | Leetcode X
     * 문제점
     * ex) [[A, B], [A,C], [C, A]] 와 같은 경로가 있다면,
     * B에서 출발하는 항공권은 없으나, 이를 확인하기 위해 순회하면서 O(n)의 비효율이 발생한다.
     * 또한, 알파벳 순으로 된 도착지 먼저 순회했을 때 완성된다면 그 뒤에 완성되더라도 틀린 답인데, 모든 경우의 수를 구해서 비교하다보니 또다시 비효율이 발생한다.
     *
     * @param tickets
     * @return
     */
//    private static boolean[] visited;
//    private static String[][] tickets;
//    private static Itinerary itinerary;
//    public String[] solution(String[][] tickets) {
//        TravelRoute.tickets = tickets;
//        TravelRoute.visited = new boolean[tickets.length];
//        TravelRoute.itinerary = new Itinerary(List.of());
//        dfs(0, "ICN", List.of("ICN"));
//        return TravelRoute.itinerary.toAnswer();
//    }
//
//    public void dfs(int visitCount, String dep, List<String> visitedList) {
//        if (visitCount == TravelRoute.tickets.length) {
//            if (TravelRoute.itinerary.isEmpty()) {
//                TravelRoute.itinerary = new Itinerary(visitedList);
//            } else {
//                Itinerary other = new Itinerary(visitedList);
//                TravelRoute.itinerary = TravelRoute.itinerary.compareTo(other) < 0 ? TravelRoute.itinerary : other ;
//            }
//            return;
//        }
//        for (int i = 0; i < tickets.length; i++) {
//            if (!visited[i] && tickets[i][0].equals(dep)) {
//                visited[i] = true;
//                List<String> copyList = new ArrayList<>(visitedList);
//                copyList.add(tickets[i][1]);
//                dfs(visitCount + 1, tickets[i][1], copyList);
//                visited[i] = false;
//            }
//        }
//    }
//    private static class Itinerary implements Comparable<Itinerary> {
//        private final List<String> plan;
//
//        private Itinerary(List<String> plan) {
//            this.plan = plan;
//        }
//
//        public boolean isEmpty() {
//            return plan.isEmpty();
//        }
//
//        @Override
//        public int compareTo(Itinerary o) {
//            String flatPlan = this.plan.stream().reduce("", (x1, x2) -> x1 + x2);
//            String flatOtherPlan = o.plan.stream().reduce("", (x1, x2) -> x1 + x2);
//            return flatPlan.compareTo(flatOtherPlan);
//        }
//
//        public String[] toAnswer() {
//            return plan.toArray(new String[0]);
//        }

    // Programmers O | Leetcode O

    /**
     * 모든 티켓은 무조건 한번이상 사용되는 것을 이용한다.
     * 알파벳 순으로 먼저 도착해야한다는 것을 이용한다.
     * HashTable을 이용해 출발지 검색의 효율을 높인다.
     *
     * @param tickets
     * @return
     */
    public String[] solution(String[][] tickets) {
        Map<String, PriorityQueue<String>> graph = new HashMap<>(tickets.length);

        Arrays.stream(tickets)
                .forEach(ticket -> graph.computeIfAbsent(ticket[0], key -> new PriorityQueue<>()).add(ticket[1]));

        Deque<String> visitedList = new LinkedList<>();
        dfs("ICN", graph, visitedList);
        return visitedList.toArray(String[]::new);
    }

    public static void dfs(String departure, Map<String, PriorityQueue<String>> graph, Deque<String> visitedList) {
        PriorityQueue<String> nextDestinations = graph.get(departure);
        while (nextDestinations != null && !nextDestinations.isEmpty()) {
            dfs(nextDestinations.poll(), graph, visitedList);
        }
        visitedList.addFirst(departure);
    }

    public static void main(String[] args) {
        TravelRoute travelRoute = new TravelRoute();
//        System.out.println(Arrays.toString(travelRoute.solution(ArrayParser.parse("[[\"ICN\", \"JFK\"], [\"HND\", \"IAD\"], [\"JFK\", \"HND\"]]", null))));
//        System.out.println(Arrays.toString(travelRoute.solution(ArrayParser.parse("[[\"ICN\", \"SFO\"], [\"SFO\", \"ATL\"], [\"ATL\", \"ICN\"], [\"ATL\",\"SFO\"], [\"ICN\", \"ATL\"], [\"SFO\",\"ICN\"], [\"ICN\", \"AAA\"]]", null))));
        System.out.println(Arrays.toString(travelRoute.solution(ArrayParser.parse("[[\"ICN\", \"SFO\"], [\"ICN\", \"ATL\"], [\"SFO\", \"ATL\"], [\"ATL\", \"ICN\"], [\"ATL\",\"SFO\"]]", null))));
    }
}
