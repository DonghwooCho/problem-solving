import sys

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

info = []
for i in range(N):
    info.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 2. 덩치 등수 계산 후 출력 하기
count = 1
res = [0 for i in range(N)]
for i in range(N):
    target = info[i]
    for j in range(N):
        if target[0] < info[j][0] and target[1] < info[j][1]:
            count += 1
    print(count, end=" ")
    count = 1
