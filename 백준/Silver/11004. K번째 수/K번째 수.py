# 1. Input data
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 2. Sort a target List
A.sort()

# 3. Output Result
print(A[K - 1])