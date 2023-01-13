import sys
import heapq

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

# 2. 최대 힙 연산 결과 출력 하기
hq = []
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num:
        heapq.heappush(hq, (-num, num))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)