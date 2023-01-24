# 1. Input information
N = int(input())
X = list(map(int, input().split()))

# 2. Calculate X_i using set 
sorted_X = list(enumerate(sorted(set(X))))
dict_X = { e[1] : e[0] for e in sorted_X}

# 3. Output results
for num in X:
    print(dict_X[num], end = ' ')