import sys


# Define dfs
def dfs(target, root, visited=[]):
    visited.append(root)
    for node in target[root]:
        if node not in visited:
            visited = dfs(target, node, visited)
    return visited


# 1. Input data
N, M = map(int, sys.stdin.readline().split())

graph = {}
for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())

    if v1 in graph:
        graph[v1].append(v2)
    else:
        graph[v1] = [v2]
    if v2 in graph:
        graph[v2].append(v1)
    else:
        graph[v2] = [v1]

# 2. Proceed dfs

# Consider recursive depth
sys.setrecursionlimit(100000000)

# Consider independent vertex
count = N - len(graph.keys())

while graph:
    count += 1
    discovered = set(dfs(graph, list(graph.keys())[0], []))
    for v in discovered:
        del graph[v]

print(count)
