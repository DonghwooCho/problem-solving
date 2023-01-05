import sys
from collections import deque

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

balloon = list(map(int, sys.stdin.readline().rstrip().split()))

# 2. 풍선 번호 출력 하기
dq = deque(enumerate(balloon), maxlen = N)
while dq:
    idx, target = dq.popleft()
    dq.rotate(-target + 1 if target > 0 else -target)
    print(idx + 1, end = " ")