from collections import Counter

# 1. 입력 받기
T = int(input())

# 2. 소인수 분해 출력 하기
for i in range(T):
    N = int(input())

    res = []
    while N != 1:
        for j in range(2, int(N ** 0.5 + 1)):
            if N % j == 0:
               res.append(j)
               N //= j
               break
        else:
            res.append(N)
            break
    res = Counter(res)
    for element in res:
        print(element, res[element])