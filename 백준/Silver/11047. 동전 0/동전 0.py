import sys

# 1. 입력 받기
N, K = map(int, sys.stdin.readline().rstrip().split())

A = [0] * N
for i in range(N):
    A[i] = int(sys.stdin.readline().rstrip())

# 2.동전 개수의 최솟값 출력 하기
res = 0
while K:
    if K >= A[-1]:
        res += K // A[-1]
        K %= A[-1]
    
    A.pop()

print(res)