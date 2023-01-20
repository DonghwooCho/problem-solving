n = int(input())
targets = list(map(int, input().split()))

targets.sort()
for i in range(n):
    print(targets[i], end = ' ')