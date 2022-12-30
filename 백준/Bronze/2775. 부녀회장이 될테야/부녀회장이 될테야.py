import sys

# 1. 입력 받기
T = int(sys.stdin.readline().rstrip())

k = []
n = []
for i in range(T):
    k.append(int(sys.stdin.readline().rstrip()))
    n.append(int(sys.stdin.readline().rstrip()))

# 2. 해당 집 거주민 수 출력
apartment = [[i + 1 for i in range(14)]]
total = 0

# 테스트 케이스 순회
for x in range(T):
    if k[x] == 0:
        print(n[x])
        continue
    for i in range(1, 15):
        apartment.append([])
        for j in range(14):
            total = apartment[i - 1][j]

            if j != 0:
                total += apartment[i][j - 1]
            apartment[i].append(total)

            if(k[x] == i and n[x] == j + 1):
                print(total)