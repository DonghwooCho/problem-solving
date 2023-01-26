# 1. Input data
X, Y = map(int, input().split())

Z = Y * 100 // X

# 2. Find minimum number of playing games
if Z == 99 or Z == 100:
    print(-1)
else:
    lo = 1
    hi = X
    while lo <= hi:
        mid = (lo + hi) // 2

        if Z == (Y + mid) * 100 // (X + mid):
            lo = mid + 1
        else:
            hi = mid - 1

# 3. Output result
    print(lo)
