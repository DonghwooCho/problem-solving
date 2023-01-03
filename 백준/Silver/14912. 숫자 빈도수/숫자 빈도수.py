# 1. 입력 받기
n, d = map(int, input().split())

# 2. 빈도수 출력
count = 0
for i in range(1, n + 1):
    n_str = str(i)
    for j in range(len(n_str)):
        if int(n_str[j]) == d:
            count += 1

print(count)