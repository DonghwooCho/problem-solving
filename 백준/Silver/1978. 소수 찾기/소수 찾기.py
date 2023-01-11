# 1. 입력 받기
n = int(input())
targets = list(map(int, input().split()))

# 2. 소수 개수 출력
count = 0
for target in targets:
    if target == 1:
        continue
    else:
        count += 1
        for i in range(2, target):
           if target % i == 0:
                count -= 1
                break

print(count)