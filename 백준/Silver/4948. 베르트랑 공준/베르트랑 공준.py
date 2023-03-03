def erasto(n):
    check = [True] * (2 * n + 1)
    check[0] = check[1] = False
    for i in range(2, int((2 * n) ** 0.5) + 1):
        if check[i]:
            for j in range(i + i, 2 * n + 1, i):
                check[j] = False

    count = 0
    for i in range(n + 1, 2 * n + 1):
        if check[i]:
            count += 1

    return count


n = int(input())
while n != 0:
    if n == 1:
        print(1)
    else:
        print(erasto(n))
    n = int(input())
