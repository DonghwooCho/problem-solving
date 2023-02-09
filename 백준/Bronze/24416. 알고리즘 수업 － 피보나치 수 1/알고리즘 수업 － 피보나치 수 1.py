global count_recursion
global count_dp


# Define fibonacci(recursion)
def fib_recursion(n):
    global count_recursion
    if n == 1 or n == 2:
        count_recursion += 1
        return 1
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)


# Define fibonacci(dp)
def fib_dp(n):
    global count_dp
    fib = [0] * n
    fib[0] = fib[1] = 1
    if n >= 2:
        for i in range(2, n):
            count_dp += 1
            fib[i] = fib[i - 1] + fib[i - 2]
    return fib


# 1. Input data
N = int(input())

count_recursion = 0
count_dp = 0

# 2. Output result
fib_recursion(N)
fib_dp(N)

print(count_recursion, count_dp)
