from sys import stdin

# 1. 입력 받기
N, M = map(int, stdin.readline().split())

# 2. 출력 하기
print(N - M if N >= M else M - N)