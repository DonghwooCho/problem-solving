# 1. 입력 받기
N = int(input())
A = list(map(int, input().split()))

# 2. 결과 출력 하기
print(min(A) * max(A))