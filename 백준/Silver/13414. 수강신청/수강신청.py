import sys


K, L = map(int, sys.stdin.readline().rstrip().split())

student_ids = {}
for i in range(L):
    student_ids[sys.stdin.readline().rstrip()] = i


ordered_ids = dict(sorted(student_ids.items(), key=lambda x: x[1]))
result_ids = list(ordered_ids.keys())

for i in range(len(result_ids)):
    if i >= K:
        break
    else:
        print(result_ids[i])
