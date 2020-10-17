
import java.io.BufferedReader;
import java.util.*;
import java.util.function.Function;

public class ProblemC {

    public static int[] readInts(Scanner s) {
        String[] strings = s.nextLine().split(" ");
        int[] ints = new int[strings.length];

        for (int i  = 0; i < ints.length; i++) {
            ints[i] = Integer.parseInt(strings[i]);
        }
        return ints;
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int[] top = readInts(s);
        int numPoints = top[0];
        int numWalkways = top[1];

        int[] points = readInts(s);
        int start = points[0];
        int end = points[1];

        Map<Integer, Map<Integer, Integer>> edges = new HashMap<>();
        Map<Integer, Integer> table = new HashMap<>();
        table.put(end, Integer.MAX_VALUE);

        Function<Integer, Map<Integer, Integer>> makeMap = x -> new HashMap<>();

        for (int i = 0; i < numWalkways; i++) {
            int[] line = readInts(s);
            edges.computeIfAbsent(line[0], makeMap).put(line[1], line[2]);
            edges.computeIfAbsent(line[1], makeMap).put(line[0], line[2]);
        }

        Set<Integer> seen = new HashSet<>();
        Queue<Map.Entry<Integer, Integer>> queue = new PriorityQueue<>(
                Comparator.comparing(x -> -x.getKey()));

        queue.add(new AbstractMap.SimpleImmutableEntry<>(Integer.MAX_VALUE, end));

        while (!queue.isEmpty()) {
            System.out.println(queue);
            Map.Entry<Integer, Integer> x = queue.poll();
            if (!seen.add(x.getValue())) {
                continue;
            }

            for (Map.Entry<Integer, Integer> e : edges.getOrDefault(x.getValue(), Collections.emptyMap()).entrySet()) {
                int inc = e.getKey();
                int weight = e.getValue();
                if (seen.contains(inc))
                    continue;

                int y = Math.min(table.getOrDefault(x.getValue(), Integer.MAX_VALUE), weight);
                if (y > table.getOrDefault(inc, 0)) {
                    table.put(inc, y);
                    queue.add(new AbstractMap.SimpleImmutableEntry<>(y, inc));
                }
            }
        }

        System.out.println(table.get(start));

    }
}
/*

edges = defaultdict(dict)
table = defaultdict(lambda: 0)
table[end] = float('inf')

for x in range(num_walks):
    a, b, w = [int(x) for x in input().split()]
    edges[a][b] = w
    edges[b][a] = w

from collections import deque
from queue import PriorityQueue

print(edges)

seen = set()
q = PriorityQueue()
q.put((-table[end], end))

while q:
    x = q.get_nowait()
    if x in seen:
        continue
    seen.add(x)
    print(x)

    for inc in edges[x]:
        print(inc)
        if inc in seen: continue

        y = min(table[end], edges[x][inc])
        if y > table[inc]:
            table[inc] = y
            q.put((-table[inc], inc))
 */