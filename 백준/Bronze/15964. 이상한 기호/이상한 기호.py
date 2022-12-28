from sys import stdin

# 1. 입력 받기
A, B = map(int, stdin.readline().rstrip().split())

# 2. 수식 계산 후 출력 하기
def func_15964(x, y):
    return (x + y) * (x - y)

print(func_15964(A, B))