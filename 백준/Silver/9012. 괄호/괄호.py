import sys

# 1. 입력 받기
T = int(sys.stdin.readline().rstrip())

stack = []
target = []

# 2. VPS 여부 출력하기
for i in range(T):
    stack = []
    target = sys.stdin.readline().rstrip()
    for j in range(len(target)):
        if "(" == target[j]:
            stack.append(target[j])
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        print("NO" if stack else "YES")