import sys

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

points = [0] * N
for i in range(N):
    points[i] = list(map(int, sys.stdin.readline().rstrip().split()))

# 2. 정렬한 좌표 출력 하기
points.sort(key = lambda point: point[1])
points.sort(key = lambda point: point[0])

for point in points:
    print(point[0], point[1])