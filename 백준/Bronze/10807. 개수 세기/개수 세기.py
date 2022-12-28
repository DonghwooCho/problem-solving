from sys import stdin

# 1. 입력 받기
N = int(stdin.readline().rstrip())
num_list = list(map(int, stdin.readline().rstrip().split()))
v = int(stdin.readline().rstrip())

count = 0
# 2. v계산 후 출력 하기
for num in num_list:
    if num == v:
        count += 1

print(count)