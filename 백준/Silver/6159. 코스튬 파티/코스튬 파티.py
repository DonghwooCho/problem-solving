import sys

# 1. 입력 받기
N, S = map(int, sys.stdin.readline().rstrip().split())

cows = [0] * N
for i in range(N):
    cows[i] = int(sys.stdin.readline().rstrip())

# 2. 결과 출력 하기
count = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if cows[i] + cows[j] <= S:
            count += 1

print(count)