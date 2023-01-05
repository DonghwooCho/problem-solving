import sys
from collections import deque

# 1. 입력 받기
T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    alphabet = deque(list(sys.stdin.readline().rstrip().split()))

# 2. 카드 문자열 계산 후 출력
    dq = deque([alphabet[0]])
    alphabet.popleft()
    while len(alphabet) != 0:
        target = alphabet[0]
        alphabet.popleft()

        if dq[0] >= target:
            dq.appendleft(target)
        else:
            dq.append(target)

    while len(dq) != 0:
        print(dq[0], end = "")
        dq.popleft()
    
    print()