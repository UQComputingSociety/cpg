from collections import defaultdict

num_people, num_edges, num_events = [int(x) for x in input().split()]

adjacents = defaultdict(set)

for x in range(num_edges):
    a, b = [int(x) for x in input().split()]
    adjacents[a].add(b)
    adjacents[b].add(a)

# print(adjacents)

events = []

# going in reverse time.
for x in range(num_events):
    t, a, b = input().split()
    a, b = int(a), int(b)
    events.append((t, a, b))

    if t == 'E':
        adjacents[a].remove(b)
        adjacents[b].remove(a)

cluster = {}
for a in range(num_people + 1):
    cluster[a] = { a }

def merge_clusters(a, b):
    cluster_a = cluster[a]
    cluster_b = cluster[b]
    if cluster_a is cluster_b:
        return
    if len(cluster_a) > len(cluster_b):
        for x in cluster_b:
            cluster_a.add(x)
            cluster[x] = cluster_a
    else:
        for x in cluster_a:
            cluster_b.add(x)
            cluster[x] = cluster_b

# print(num_people)
# dfs
for a in adjacents:
    for b in adjacents[a]:
        merge_clusters(a, b)

output = []
for t, a, b in reversed(events):
    if t == 'S':
        output.append(cluster[a] is cluster[b])
    else:
        merge_clusters(a, b)

for x in reversed(output):
    print('YES' if x else 'NO')
