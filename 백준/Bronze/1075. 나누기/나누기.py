# 1. 입력 받기
N = int(input())
F = int(input())

# 2. 정답 구하고 출력
N = list(str(N))

for i in range(100):
    N[-2] = str(i // 10)
    N[-1] = str(i % 10)
    temp = int("".join(N))
    if temp % F == 0:
        print("%02d" % (i))
        break