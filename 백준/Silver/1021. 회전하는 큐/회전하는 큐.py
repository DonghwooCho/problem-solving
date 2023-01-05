import sys
from collections import deque

# 1. 입력 받기
N, M = map(int, sys.stdin.readline().rstrip().split())

location = list(map(int, sys.stdin.readline().rstrip().split()))

# 2. 회전하는 큐 구현 하기
dq = deque([i + 1 for i in range(N)], maxlen=N)
cnt = 0

for i in location:
    if i == dq[0]:
        dq.popleft()
    else:
        if dq.index(i) < len(dq) - dq.index(i):
            while dq[0] != i:
                dq.rotate(-1)
                cnt += 1
        else:
            while dq[0] != i:
                dq.rotate(1)
                cnt += 1
        dq.popleft()

print(cnt)