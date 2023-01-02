# 1. 입력 받기
N = int(input())

# 2. N 이하인 신기한 수의 개수 출력
count = 0
for i in range(1, N + 1): #zeroDivisionError 주의
    if i % sum(list(map(int, str(i)))) == 0:
        count += 1

print(count)