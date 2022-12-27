import sys
import math

# 1. 입력 받기
N, M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

# 2. 적어도 M미터를 집에 가져가기 위해 설정할 수 있는 최댓값 구하기(이진 탐색, binary search)
trees.sort()

start = 0

end = trees[-1]

mid = (start + end) // 2

count = 0
while start <= end:

    for tree in trees:
        if tree - mid >= 0:
            count += tree - mid
        if count >= M:
            break

    if count >= M:
        start = mid + 1 
    else:
        end = mid - 1
    
    count = 0
    mid = (start + end) // 2

print(end)