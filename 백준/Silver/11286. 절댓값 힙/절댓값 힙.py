import heapq
import sys

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

# 2. 요구값 출력 하기
hq = []
for i in range(N):
    num = int(sys.stdin.readline().rstrip())

    if num:
        heapq.heappush(hq, (abs(num), num))

    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)