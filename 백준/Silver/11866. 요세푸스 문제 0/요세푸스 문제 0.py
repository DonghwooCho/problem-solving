from collections import deque

# 1. 입력 받기
N, K = map(int, input().split())

# 2. 요세푸스 순열 출력 하기
targets = deque(list(i + 1 for i in range(N)))

print('<', end = '')

while len(targets) != 1:
    targets.rotate(-K + 1)
    print(targets[0], end = ', ')
    targets.popleft()

print(targets[0], end = '')
print('>')