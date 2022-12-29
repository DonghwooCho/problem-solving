import sys

# 1. 입력 받기
length_list = []
length = []
while length != [0, 0, 0]:
    length = list(map(int, sys.stdin.readline().rstrip().split()))
    length_list.append(length)

# 2. 직각삼각형 여부 출력 하기
for i in range(len(length_list) - 1):
    length_list[i].sort()
    if(length_list[i][2]**2 == length_list[i][0]**2 + length_list[i][1]**2):
        print("right")
    else:
        print("wrong")