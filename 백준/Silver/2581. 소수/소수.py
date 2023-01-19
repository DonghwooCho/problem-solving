def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input())
M = int(input())

res = []
for i in range(N, M + 1):
    if is_prime(i):
       res.append(i)

if not res:
    print(-1)
else:
    print(sum(res), min(res), sep = '\n')