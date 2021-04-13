from collections import defaultdict

succ = defaultdict(lambda: dict())
w = int(input().split(" ")[1])
c, v = [int(i) for i in input().split(" ")]

for i in range(w):
    s, e, wi = tuple([int(i) for i in input().split(" ")])
    succ[s][e] = wi
    succ[e][s] = wi

from functools import lru_cache

@lru_cache(maxsize=2**8)
def visit(node, visitedNodes):
    if node == v:
        return float('inf')
    succs = succ[node]
    ress = []
    for s in succs.keys():
        if s not in visitedNodes:
            temp = visitedNodes | { s }
            res = visit(s, temp)

            if (res !=  None):
                ress.append((s, res))
    
    if len(ress) == 0:
        return None
    
    maxx = max(ress, key=lambda x: min(x[1], succs[x[0]]))

    return min(maxx[1], succs[maxx[0]])

print(visit(c, frozenset([c])))
