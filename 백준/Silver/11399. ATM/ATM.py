from collections import deque

# 1. 입력 받기
N = int(input())
P = list(map(int, input().split()))

# 2. 인출하는데 필요한 시간의 최솟값 출력 하기
res = 0
temp = 0
P.sort()
P = deque(P)
while P:
    temp += P.popleft()
    res += temp
print(res)
