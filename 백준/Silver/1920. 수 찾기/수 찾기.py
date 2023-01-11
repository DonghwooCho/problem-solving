import sys
from collections import Counter

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

A = list(map(int, (sys.stdin.readline().rstrip().split())))
A_count = Counter(A)

# 2. 존재 여부 출력 하기
M = int(sys.stdin.readline().rstrip())

targets = list(map(int, (sys.stdin.readline().rstrip().split())))
for target in targets:
    if A_count[target] != 0:
        print(1)
    else:
        print(0)