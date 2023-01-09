# 1. 입력 받기
change = 1000 - int(input())

# 2. 잔돈에 포함된 매수 출력
res = change // 500
change %= 500
res += change // 100
change %= 100
res += change // 50
change %= 50
res += change // 10
change %= 10
res += change // 5
change %= 5
res += change

print(res)