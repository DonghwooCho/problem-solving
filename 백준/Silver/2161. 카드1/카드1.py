from collections import deque

n = int(input())
targets = deque([i + 1 for i in range(n)])

while targets:
    print(targets.popleft(), end = ' ')
    targets.rotate(-1)