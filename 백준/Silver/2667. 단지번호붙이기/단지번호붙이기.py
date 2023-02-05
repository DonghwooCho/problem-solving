import sys
global count
sys.setrecursionlimit(1000000)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# Define dfs
def dfs(row, col):
    global count
    if field[row][col] == 1:
        field[row][col] = 0
        count += 1

    for d in range(4):
        if 0 <= row + dy[d] < N and 0 <= col + dx[d] < N:
            if field[row + dy[d]][col + dx[d]] == 1:
                dfs(row + dy[d], col + dx[d])


# 1. Input data
N = int(input())

field = []
for i in range(N):
    field.append(list(map(int, list(input()))))

res = []
for i in range(N):
    for j in range(N):
        count = 0
        if field[i][j] == 1:
            dfs(i, j)
            res.append(count)


# 2. Output result
res.sort()
print(len(res))
for i in res:
    print(i)
    