import sys
import heapq

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

hq = []
for i in range(N):
    heapq.heappush(hq, int(sys.stdin.readline().rstrip()))

# 2. 비교 최솟값 출력 하기

res = 0
while len(hq) >= 2:
    temp = heapq.heappop(hq) + heapq.heappop(hq)
    res += temp
    heapq.heappush(hq, temp)

print(0 if N == 1 else res)