# 1. 입력 받기
N, M = map(int, input().split())

# 2. 최대공약수, 최소공배수 출력하기
gcd = 1
for i in range(1, min(N, M) + 1):
    if N % i == 0 and M % i == 0:
        gcd = i

lcm = N * M // gcd
# for i in range(1, N * M):
#     if i % N == 0 and i % M == 0:
#         lcm = i
#         break

print(gcd)
print(lcm)