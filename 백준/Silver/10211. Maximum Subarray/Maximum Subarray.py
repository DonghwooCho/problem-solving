import sys

# 1. 입력 받기
T = int(sys.stdin.readline().rstrip())

N = 0
X = []

for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    X = list(map(int, sys.stdin.readline().rstrip().split()))
# 2. maximum subarray의 합 출력(동적 프로그래밍)
    dp = [i for i in X]
    for j in range(1, N):
        dp[j] = max(dp[j - 1] + X[j], X[j])

    print(max(dp))