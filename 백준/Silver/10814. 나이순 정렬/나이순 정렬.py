# 1. 입력 받기
N = int(input())

# 2. 정렬 후 출력 하기
members = []
for i in range(N):
    members.append(list(input().split()))
members.sort(key = lambda member: int(member[0]))

for member in members:
    print(member[0], member[1], end = ' ')