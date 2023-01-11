import sys

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

nums = [0] * N
for i in range(N):
    nums[i] = int(sys.stdin.readline().rstrip())

# 2. 오름차순 출력 하기
nums.sort()

for num in nums:
    print(num)