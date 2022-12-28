import sys
from math import factorial

# 1. 입력 받기
N = int(sys.stdin.readline())

# 2. N! 구하기
result =  factorial(N)

# 3. 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하기
result_list = list(str(result))

count = 0

reverse_result_list = list(reversed(result_list))
for i in range(len(reverse_result_list)):
    if reverse_result_list[i] != '0':
        break
    else:
        count += 1

print(count)