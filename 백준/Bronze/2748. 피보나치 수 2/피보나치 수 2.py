def fibo(n):
    fibo_list = [0, 1]
    for i in range(2, n + 1):
        fibo_list.append(fibo_list[i - 2] + fibo_list[i - 1])
    return fibo_list[-1]

print(fibo(int(input())))