import math

# 1. 입력 받기
N = int(input())
r = list(map(int, input().split()))

# 2. 바퀴 수 출력 하기
movement = r[0]
for i in range(1, N):
    print(movement // math.gcd(movement, r[i]), '/', r[i] // math.gcd(movement, r[i]), sep= '')