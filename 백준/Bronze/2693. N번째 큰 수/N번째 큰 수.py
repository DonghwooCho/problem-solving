T = int(input())
for i in range(T):
    target = list(map(int, input().split()))
    target.sort()
    print(target[-3])
    