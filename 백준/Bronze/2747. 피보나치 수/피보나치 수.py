def fibo(n):
    fibo_list = [0, 1]
    for i in range(2, n + 1):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])

    return fibo_list

n = fibo(int(input()))
if n == 0:
    print(0)
elif n == 1 or n == 2:
    print(1)
else:
    print(n[-1])