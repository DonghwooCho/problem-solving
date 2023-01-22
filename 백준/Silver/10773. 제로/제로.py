import sys

# 1. 입력 받기
K = int(sys.stdin.readline())

stack = []
for i in range(K):
    stack.append(int(sys.stdin.readline()))
    if stack[-1] == 0:
        stack.pop()
        stack.pop()

# 2. 적어낸 수 합 출력 하기
print(sum(stack))