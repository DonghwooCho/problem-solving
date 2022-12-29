import sys
import math

# 1. 입력 받기
A, B, V = map(int, sys.stdin.readline().rstrip().split())

height = 0
day = 0
# 2. 올라가는 데 걸리는 기간 구하기
if A >= V:
    print(1)
else:
    print(math.ceil((V-A) / (A-B)) + 1) 