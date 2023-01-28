from collections import deque


# Define DFS
def dfs(target, root, visited=[]):
    visited.append(root)
    print(root, end=' ')

    target[root].sort()
    for node in target[root]:
        if node not in visited:
            visited = dfs(target, node, visited)
    return visited


# Define BFS
def bfs(target, root, visited=[]):
    queue = deque([root])
    visited.append(root)
    print(root, end=' ')

    while queue:
        v = queue.popleft()
        target[v].sort()
        for node in target[v]:
            if node not in visited:
                queue.append(node)
                visited.append(node)
                print(node, end=' ')
    return visited


# 1. Input data
N, M, V = map(int, input().split())

graph = {}
for i in range(M):
    v1, v2 = map(int, input().split())
    if v1 in graph:
        graph[v1].append(v2)
    else:
        graph[v1] = [v2]
    if v2 in graph:
        graph[v2].append(v1)
    else:
        graph[v2] = [v1]


# 2. Proceed dfs and bfs
if V in graph:
    dfs(graph, V)
    print()
    bfs(graph, V)
# Consider independent vertex
else:
    print(V, V, sep='\n')
