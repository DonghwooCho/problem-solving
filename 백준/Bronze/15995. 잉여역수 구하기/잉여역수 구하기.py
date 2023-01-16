# 1. 입력 받기
a, m = map(int, input().split())

# 2. 잉여역수 출력 하기
x = 1
while (a * x) % m != 1:
    x += 1

print(x)