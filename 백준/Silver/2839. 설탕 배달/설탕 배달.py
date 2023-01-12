# 1. 입력 받기
N = int(input())

# 2. 봉지의 최솟값 출력 하기
if N % 5 == 0:
    print(N // 5)
else:
    res = N
    count = 1
    while N - count * 5 > 0:
        temp = N - count * 5
        if temp % 3 == 0:
            res = count + temp // 3
            count += 1
        else:
            count += 1

    if res <= N // 3:
        print(res)
    else:
        if N % 3 == 0:
            print(N // 3)
        else:
            print(-1)