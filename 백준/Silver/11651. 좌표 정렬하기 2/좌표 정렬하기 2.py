import sys

N = int(sys.stdin.readline())
targets = []
for i in range(N):
    targets.append(list(map(int, sys.stdin.readline().split())))

targets.sort(key=lambda x: x[0])
targets.sort(key=lambda x: x[1])

for target in targets:
    print(target[0], target[1])