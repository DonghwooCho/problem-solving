# 소수 판정 함수 정의
def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 1. 입력 받기
T = int(input())

for i in range(T):
    n = int(input())

# 2. 골드바흐 파티션 출력 하기
    for j in range(n // 2, 1, -1):
        if is_prime(j) and is_prime(n - j):
            print(j, n - j)
            break