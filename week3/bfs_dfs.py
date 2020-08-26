def bfs(graph, root): 
    visited = set()
    queue = [root]
    while queue: 
        vertex = queue.pop(0)
        print(vertex)
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour)

def dfs(graph, root):
    visited = set()
    stack = [root]
    while stack:
        vertex = stack.pop()
        print(vertex)
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

graph = {0: set([1,2]),
         1: set([3,4]),
         2: set([5,6]),
         3: set(),
         4: set(),
         5: set(),
         6: set()}

print(bfs(graph, 0))
print(dfs(graph, 0))
