import sys

N = int(sys.stdin.readline().rstrip())

targets = [0] * 10000
for i in range(N):
    targets[int(sys.stdin.readline().rstrip()) - 1] += 1

for i in range(10000):
    for j in range(targets[i]):
        print(i + 1)