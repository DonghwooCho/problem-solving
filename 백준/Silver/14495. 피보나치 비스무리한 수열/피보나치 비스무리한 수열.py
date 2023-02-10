# Define fib_similar
def fib_similar(n):
    fib = [1, 1, 1]
    for i in range(3, n):
        fib.append(fib[i - 1] + fib[i - 3])

    return fib[-1]


print(fib_similar(int(input())))
