import sys
sys.setrecursionlimit(1000000)
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]


# Define dfs
def dfs(y, x):
    for d in range(8):
        if 0 <= y + dy[d] < h and 0 <= x + dx[d] < w:
            if visited[y + dy[d]][x + dx[d]] == 1:
                visited[y + dy[d]][x + dx[d]] = 0
                dfs(y + dy[d], x + dx[d])


# 1. Input data
while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break

    visited = []
    for i in range(h):
        visited.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 2. Count targets
    count = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 1:
                count += 1
                dfs(i, j)

    print(count)
