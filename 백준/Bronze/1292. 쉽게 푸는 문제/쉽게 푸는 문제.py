A, B = map(int, input().split())
target = []
for i in range(1, 1000):
    for j in range(i):
        if len(target) < 1000:
            target.append(i)

hap = 0
for i in range(A, B + 1):
    hap += target[i - 1]

print(hap)
