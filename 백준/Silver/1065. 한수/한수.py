# 1. 입력 받기
N = input()

# 2. 조건을 만족하는 한수의 개수 출력
if int(N) <= 99:
    print(N)
else:
    count = 99
    for i in range(100, int(N) + 1):
        res = list(map(int, str(i)))
        j = 0
        while j + 2 < len(res):
            if res[j + 1] * 2 == res[j] + res[j + 2]:
                j += 1
            else:
                break
            if j + 2 == len(res):
                count += 1
    print(count)

    