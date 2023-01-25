# 1. Input data
N = int(input())
money = list(map(int, input().split()))
M = int(input())

# 2. Find maximum solution
lo = 0
hi = max(money)

while lo <= hi:
    mid = (lo + hi) // 2
    remainder = 0

    for e in money:
        if mid - e > 0:
            remainder += mid - e

    if M > mid * N - remainder:
        lo = mid + 1
    elif M == mid * N - remainder:
        print(mid)
        hi = 0
        break
    else:
        hi = mid - 1

# 3. Output result
if hi:
    print(hi)
