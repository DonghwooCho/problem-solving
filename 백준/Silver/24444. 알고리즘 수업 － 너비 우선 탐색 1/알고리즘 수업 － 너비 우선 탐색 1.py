import sys
from collections import deque
global order


# Define bfs
def bfs(start):
    global order

    visited[start] = order
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if visited[node] == 0:
                order += 1
                visited[node] = order
                queue.append(node)


# 1. Input data
N, M, R = map(int, sys.stdin.readline().rstrip().split())
graph = {key + 1: [] for key in range(N)}
visited = {key + 1: 0 for key in range(N)}

for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for key in range(N):
    graph[key + 1].sort()

# 2. Proceed bfs
order = 1
bfs(R)
for res in visited.values():
    print(res)
