# Define dfs
def dfs(target, root, visited=[], count=0):
    visited.append(root)
    for node in target[root]:
        if node not in visited:
            count += 1
            visited, count = dfs(target, node, visited, count)
    return visited, count


# 1. Input data
node_size = int(input())
T = int(input())

graph = {}
for i in range(T):
    v1, v2 = map(int, input().split())

    if v1 in graph:
        graph[v1].append(v2)
    else:
        graph[v1] = [v2]
    if v2 in graph:
        graph[v2].append(v1)
    else:
        graph[v2] = [v1]

# 2. Process dfs
if graph[v1]:
    print(dfs(graph, 1)[1])
else:
    print(0)
