import sys

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

# 2. 생성자의 최솟값 출력
target = []
min = 0
for i in range(1, N):
    target = list(map(int, list(str(i))))
    # for j in range(0, len(target)):
    #     target[j] = int(target[j]) * ((10 ** (len(target) - j - 1)) + 1)
    # if N == sum(target):
    #     min = i
    if N == sum(target) + i:
        min = i
        break

print(min)