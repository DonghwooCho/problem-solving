from sys import stdin

# 1. 입력 받기
num_list = []
for i in range(28):
    num_list.append(int(stdin.readline().rstrip()))

# 2. v계산 후 출력 하기
for i in range(30):
    if i + 1 not in num_list:
        print(i + 1)