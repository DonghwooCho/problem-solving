N = input()
if len(N) == 3:
    if N[0:2] == '10':
        print(10 + int(N[-1]))
    else:
        print(int(N[0]) + 10)
elif len(N) == 4:
    print(20)
else:
    print(int(N[0]) + int(N[1]))