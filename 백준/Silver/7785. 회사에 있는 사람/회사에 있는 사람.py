from collections import deque

n = int(input())
targets = {}
for i in range(n):
    name, action = input().split()
    targets[name] = action

res = sorted(targets.items(), key = lambda x: x[0], reverse = True)
for i in res:
    if i[1] == 'enter':
        print(i[0])