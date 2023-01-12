# 1. 입력 받기
A, B = input().split()

# 2. 최솟값과 최댓값 출력 하기
A = A.replace('6', '5')
B = B.replace('6', '5')

print(int(A) + int(B), end = ' ')

A = A.replace('5', '6')
B = B.replace('5', '6')

print(int(A) + int(B))