import sys
from collections import Counter # 리스트에 각 원소가 몇 번 사용되었는지 확인 가능

# 1. 입력 받기
length = int(sys.stdin.readline())

num_list = []
for i in range(0, length):
    num_list.append(int(sys.stdin.readline()))

# 2. 산술 평균
print(round(sum(num_list)/length))

# 3. 중앙값
num_list.sort()
print(num_list[length // 2 - 1 if length % 2 == 0 else length // 2])

# 4. 최빈값
length_list = sorted(Counter(num_list).items(), key=lambda x: x[1])

temp_list = []
for i in range(0, len(length_list)):
    if length_list[i][1] == length_list[-1][1]:
        temp_list.append(length_list[i][0])

temp_list.sort()
print(temp_list[0] if len(temp_list)==1 else temp_list[1])

# 5. 범위
print(num_list[-1] - num_list[0])