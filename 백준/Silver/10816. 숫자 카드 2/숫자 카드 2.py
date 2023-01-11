import sys
from collections import Counter

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())
A = list(map(int, (sys.stdin.readline().rstrip().split())))
A_count = Counter(A)

# 2. 개수 출력 하기
M = int(sys.stdin.readline().rstrip())
targets = list(map(int, (sys.stdin.readline().rstrip().split())))

for target in targets:
    print(A_count[target], end = ' ')