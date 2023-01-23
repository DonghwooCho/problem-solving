import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().rstrip().split())

people = [0] * (N + M)
for i in range(N + M):
    people[i] = sys.stdin.readline().rstrip()

people_count = Counter(people)
target = list(people_count.items())
target.sort(key = lambda x: x[0])

count = 0
res = []
for k, v in target:
    if v == 2:
        count += 1
        res.append(k)

print(count)
for k in res:
    print(k)