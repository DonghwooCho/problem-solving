def erasto(M, N):
    res = N * [True]
    res[0] = False
    res[1] = False
    for i in range(2, int(N ** 0.5) + 1):
        if res[i]:
            for j in range(i + i, N, i):
                res[j] = False

    return [i for i in range(M, N) if res[i]]


M, N = map(int, input().split())
for i in erasto(M, N + 1):
    print(i)
