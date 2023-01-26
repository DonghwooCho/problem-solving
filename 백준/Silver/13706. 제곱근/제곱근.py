# 1. Input Data
N = int(input())

# 2. Find square root
lo = 1
hi = N
while lo != hi:
    mid = (lo + hi) // 2

    if mid ** 2 == N:
        break
    elif mid ** 2 > N:
        hi = mid - 1
    else:
        lo = mid + 1

# 3. Output result
print(mid if mid ** 2 == N else lo)