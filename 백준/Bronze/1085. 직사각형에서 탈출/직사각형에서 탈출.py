import sys

# 1. 입력 받기
x, y, w, h = map(int, sys.stdin.readline().rstrip().split())

# 2. 최솟값 구하고 출력 하기
distances = [w - x, x, y, h - y]
print(min(distances))