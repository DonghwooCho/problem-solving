from math import factorial

# 1. 입력 받기
n, k = map(int, input().split())

# 2. 이항 계수 출력
print((factorial(n)//factorial(n-k)) // factorial(k))