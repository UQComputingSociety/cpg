num_points, num_walks = [int(x) for x in input().split()]

start, end = [int(x) for x in input().split()]

from collections import defaultdict

edges = defaultdict(dict)
table = defaultdict(lambda: 0)
table[end] = float('inf')

for x in range(num_walks):
    a, b, w = [int(x) for x in input().split()]
    edges[a][b] = w
    edges[b][a] = w 

from collections import deque 
from queue import PriorityQueue

seen = set()
q = PriorityQueue()
q.put((table[end], end))

while q:
    print(q.queue)
    x = q.get_nowait()
    if x[1] in seen:
        continue
    seen.add(x[1])
    
    for inc in edges[x[1]]:
        print(inc)
        if inc in seen: continue

        y = min(table[x[1]], edges[x[1]][inc])
        if y > table[inc]:
            print("yeah")
            table[inc] = y
            q.put((table[inc], inc))
    
print(table[start])