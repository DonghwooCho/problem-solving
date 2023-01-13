from collections import deque
import sys

# 1. 입력 받기
N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# 2. 최솟값 출력 하기
dq = deque([])
for i in range(N):
    if dq and dq[0][0] <= i - L:
        dq.popleft()

    while dq and dq[-1][1] > A[i]:
        dq.pop()

    dq.append((i, A[i]))
    print(dq[0][1], end = ' ')