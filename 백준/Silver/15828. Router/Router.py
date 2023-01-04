import sys

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

# 2. 라우터 구현
queue = []
data = 0
while data != -1:
    data = int(sys.stdin.readline().rstrip())

    if data == 0:
        queue.pop()
    elif data == -1:
        for j in range(len(queue) - 1, -1, -1):
            print(queue[j], end=" ")
        break
    elif data > 0 and len(queue) < N:
        queue.insert(0, data)
    else:
        continue
