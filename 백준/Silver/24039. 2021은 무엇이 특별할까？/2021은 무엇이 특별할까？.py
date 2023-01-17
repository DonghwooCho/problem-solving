import math

# 1. 입력 받기
N = int(input())

# 2. 특별한 수 출력하기
primes = []
for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes.append(i)

for i in range(len(primes) - 1):
    if N < primes[i] * primes[i + 1]:
        print(primes[i] * primes[i + 1])
        break
