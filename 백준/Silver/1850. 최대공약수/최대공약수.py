import math

# 1. 입력 받기
A, B = map(int, input().split())

# 2. 최대공약수 출력 하기
print('1' * math.gcd(A, B))