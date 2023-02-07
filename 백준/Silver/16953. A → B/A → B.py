A, B = map(int, input().split())

count = 1
while B != A:
    if B % 2 == 0:
        count += 1
        B //= 2
    elif B % 10 == 1 and B != 1:
        count += 1
        B //= 10
    else:
        count = -1
        break

print(count)
