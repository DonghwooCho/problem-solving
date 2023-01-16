# 1. 입력 받기
N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

# 2. 최소 비용 출력 하기
cost = 0
temp_length = 0
temp_price = 0
for i in range(N - 1):
    temp_price = temp_price if temp_price else price[i]
    temp_length += length[i]

    if price[i] >= price[i + 1]:
        cost += temp_price * temp_length
        temp_length = 0
        temp_price = 0
    else:
        temp_price = price[i] if temp_length == length[i] else temp_price

print(cost)