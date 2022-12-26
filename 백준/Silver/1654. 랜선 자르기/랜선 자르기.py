import sys

# 1. 입력 받기
# K = 이미 가지고 있는 랜선의 개수, N = 필요한 랜선의 개수
K, N = map(int, sys.stdin.readline().split())

num_list = []
for i in range(0, K):
    num_list.append(int(sys.stdin.readline()))

# 2. 랜선의 최대 길이 구하기(이진 탐색, binary search)
num_list.sort()

start = 1
end = sum(num_list) // N

mid = (start + end) // 2
ableNum = 0

while start <= end: # 조건문이 True일 때만 반복

    for num in num_list:
        ableNum += num // mid

    if N <= ableNum:
        start = mid + 1
    else:
        end = mid - 1

    mid = (start + end) // 2
    ableNum = 0

print(end)