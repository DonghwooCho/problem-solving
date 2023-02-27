T = int(input())
for i in range(T):
    s = input().split()
    for word in s:
        print(word[::-1], end = ' ')
    print()