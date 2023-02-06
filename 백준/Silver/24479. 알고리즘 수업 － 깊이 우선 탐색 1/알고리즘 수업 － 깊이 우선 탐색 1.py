import sys
global order
# Consider recursion depth
sys.setrecursionlimit(1000000)


# Define dfs
def dfs(target, start):
    global order
    if visited[start] == 0:
        visited[start] = order
        order += 1
    for node in graph[start]:
        if visited[node] == 0:
            dfs(target, node)


# 1. Input data
N, M, R = map(int, sys.stdin.readline().rstrip().split())

graph = {key + 1: [] for key in range(N)}
for i in range(M):
    v1, v2, = map(int, sys.stdin.readline().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for node in graph.keys():
    graph[node].sort()

# 2. Proceed dfs
order = 1
visited = {key + 1: 0 for key in range(N)}
dfs(graph, R)
for res in visited.values():
    print(res)
