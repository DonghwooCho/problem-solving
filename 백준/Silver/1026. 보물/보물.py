# 1. 입력 받기
N = int(input())


A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 2. 최솟값 출력 하기
A.sort()
B.sort(reverse = True)

res = 0
for i in range(N):
    res += A[i] * B[i]

print(res)