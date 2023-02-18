def fibo(n):
    fib = [0, 1, 1]
    for i in range(3, n):
        fib.append((fib[i - 1] + fib[i - 2]) % 1000000007)

    return fib[-1] % 1000000007


print(fibo(int(input())))
