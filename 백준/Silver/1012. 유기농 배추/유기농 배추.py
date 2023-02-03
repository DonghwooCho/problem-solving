from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(1000000)


# Define DFS
def dfs(target, y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for d in range(4):
        if 0 <= y + dy[d] < N and 0 <= x + dx[d] < M:
            if target[y + dy[d]][x + dx[d]]:
                target[y + dy[d]][x + dx[d]] = False
                dfs(target, y + dy[d], x + dx[d])


# 1. Input data
T = int(stdin.readline())

for i in range(T):
    M, N, K = map(int, stdin.readline().rstrip().split())
    field = [[False] * M for _ in range(N)]
    # 아래와 같이 선언 시 같은 열이 모두 같은 주소를 가리키기 때문에 에러 발생
    # field = [[False] * M] * N
    for j in range(K):
        X, Y = map(int, stdin.readline().rstrip().split())
        field[Y][X] = True

# 2. Proceed dfs
    count = 0
    for y in range(N):
        for x in range(M):
            if field[y][x]:
                dfs(field, y, x)
                count += 1

    print(count)
