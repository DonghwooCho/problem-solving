from sys import stdin

# 1. 입력 받기
N, M = map(int, stdin.readline().rstrip().split())

A = []
for i in range(N):
    A.append(list(map(int, stdin.readline().rstrip().split())))

B = []
for i in range(N):
    B.append(list(map(int, stdin.readline().rstrip().split())))

# 2. 행렬 계산 후 출력 하기
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end = ' ')
    print()