import sys
from collections import deque

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

# 2. 라우터 구현
dq = deque()
data = 0
while data != -1:
    data = int(sys.stdin.readline().rstrip())

    if data == 0:
        dq.pop()
    elif data == -1:
        while len(dq) != 0:
            print(dq[-1])
            dq.pop()
    elif data > 0 and len(dq) < N:
        dq.appendleft(data)
    else:
        continue